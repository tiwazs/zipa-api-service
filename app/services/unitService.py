import functools
from fastapi import UploadFile
from prisma import Prisma
import re

from ..services.fileService import FileService
from .unitItemService import UnitItemService
from ..models.unitDTO import UnitDTO, UnitItemCreateDTO, UnitUpdateDTO, UnitCreateDTO
from typing import List

class UnitService:
    def __init__(self, database):
        self.database = database
        self.unit_item_service = UnitItemService(database)
        self.file_service = FileService()
    
    async def get_all(self, include_items, include_faction, include_specialization) -> List[UnitDTO]:
        return await self.database.unit.find_many(
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                },
                "faction": False if not include_faction else {
                    "include": {
                        "traits": {
                            "include": {
                                "trait": {
                                    "include": {
                                        "effects": {
                                            "include": {
                                                "effect": True
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "specialization": False if not include_specialization else {
                    "include": {
                        "traits": {
                            "include": {
                                "trait": include_specialization
                            }
                        },
                        "items": {
                            "include": {
                                "item": include_specialization
                            }
                        },
                        "skills": {
                            "include": {
                                "skill": include_specialization
                            }
                        },
                    }
                },
            }
        )

    async def get_all_by_user(self, user_id, include_items, include_faction, include_specialization) -> List[UnitDTO]:
        return await self.database.unit.find_many(
            where={
                "user_id": user_id
            },
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                },
                "faction": False if not include_faction else {
                    "include": {
                        "traits": {
                            "include": {
                                "trait": {
                                    "include": {
                                        "effects": {
                                            "include": {
                                                "effect": True
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "specialization": False if not include_specialization else {
                    "include": {
                        "traits": {
                            "include": {
                                "trait": include_specialization
                            }
                        },
                        "items": {
                            "include": {
                                "item": include_specialization
                            }
                        },
                        "skills": {
                            "include": {
                                "skill": include_specialization
                            }
                        },
                    }
                },
            }
        )

    async def get_by_id(self, id: str, include_items, include_faction, include_specialization) -> UnitDTO:
        return await self.database.unit.find_unique( 
            where={"id": id},
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                },
                "faction": False if not include_faction else {
                    "include": {
                        "traits": {
                            "include": {
                                "trait": {
                                    "include": {
                                        "effects": {
                                            "include": {
                                                "effect": True
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "specialization": False if not include_specialization else {
                    "include": {
                        "traits": {
                            "include": {
                                "trait": include_specialization
                            }
                        },
                        "items": {
                            "include": {
                                "item": include_specialization
                            }
                        },
                        "skills": {
                            "include": {
                                "skill": include_specialization
                            }
                        },
                    }
                },
            }
        )

    async def get_all_extended(self, include_items, include_faction, include_specialization) -> List[UnitDTO]:
        users = await self.get_all(include_items, include_faction, include_specialization)

        return [self.extend_unit(unit) for unit in users]
    
    async def get_all_extended_by_user(self, user_id, include_items, include_faction, include_specialization) -> List[UnitDTO]:
        users = await self.get_all_by_user(user_id, include_items, include_faction, include_specialization)

        return [self.extend_unit(unit) for unit in users]
    
    async def get_extended_by_id(self, id: str, include_items, include_faction, include_specialization) -> UnitDTO:
        unit = await self.get_by_id(id, include_items, include_faction, include_specialization)

        return self.extend_unit(unit)

    async def get_by_faction_id(self, id: str, include_items) -> List[UnitDTO]:
        return await self.database.unit.find_many( 
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            },
            where={
                "factions": {
                    "some": {
                        "faction_id": id
                    }
                }
            }
        )
    
    async def create(self, unit: UnitCreateDTO) -> UnitDTO:
        # Get Unit Items
        unit_items = unit.items.copy() if unit.items else None
        del unit.items

        unit = await self.database.unit.create( 
            data=unit.dict() 
        )

        # Assign Unit Items
        try:
            if unit_items:
                for unit_item in unit_items:
                    await self.unit_item_service.create({"unit_id":unit.id, "item_id":unit_item.item_id, "quantity":unit_item.quantity})
        except Exception as e:
            await self.database.unit.delete(where={"id": unit.id})
            raise e
        
        return await self.database.unit.find_unique(
            where={"id": unit.id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def update(self, id: str, unit: UnitUpdateDTO) -> UnitDTO:
        unit_dict = unit.dict()

        # Get unit Data
        unit_current = await self.database.unit.find_unique( 
            where={"id": id} 
        )
        if(not unit_current): return None
        unit_current_dict = unit_current.dict()

        # If incomming data is empty, use current data
        for key in unit_dict:
            if unit_dict[key] is None or unit_dict[key] == "":
                unit_dict[key] = unit_current_dict[key]
        
        return await self.database.unit.update( 
            where={"id": id}, 
            data=unit_dict 
        )
    
    async def add_item(self, id: str, item_id: str, quantity: int) -> UnitDTO:
        await self.unit_item_service.create({"unit_id":id, "item_id":item_id, "quantity":quantity})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def remove_item(self, id: str, item_id: str) -> UnitDTO:
        await self.unit_item_service.delete_by_ids(id, item_id)

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def update_item(self, id: str, unit_item: UnitItemCreateDTO) -> UnitDTO:
        await self.unit_item_service.update({"unit_id": id, "item_id": unit_item.item_id, "quantity": unit_item.quantity})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def delete(self, id: str) -> UnitDTO:
        return await self.database.unit.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        unit = await self.database.unit.find_unique( 
            where={"id": id} 
        )
        if(not unit): return None

        # Save image
        filename = f"{unit.id}.jpg"
        filepath = self.file_service.save(image, "app/static/units", filename)

        return filepath

    # Extend unit. making calculations
    def value_multiplier(self, base_value: float, multiplier: float, offset: float):
        rate = 0.1
        result = ( base_value + offset )*( rate )*( multiplier )
        return result
    
    def mod_parameter_operation(self, mod_parameter_string: str, parameter: float):
        regex = '(?P<sign>[+-])?(?P<value>([\d+.]+|ND|MD|HP))?(?P<porcentage>\s*%)?(?P<max>\s*max)?'
        match = re.search(regex, mod_parameter_string)
        sign = match['sign']
        max = match['max']
        value = match['value']
        porcentage = match['porcentage']

        if(not value): return parameter

        result = parameter

        if(porcentage and sign == '+'):
            result += result * (float(value) / 100)
        elif(porcentage and sign == '-'):
            result -= result * (float(value) / 100)
        elif(sign == '+'):
            result += float(value)
        elif(sign == '-'):
            result -= float(value)
        

        return result

    def weight_penalty(self, strength: float, weight: float, strength_rate: float):
        strength_modified = strength * strength_rate
        if(weight < strength_modified/4):
            return 0
        elif(weight < strength_modified/2):
            return 1
        elif(weight < 3*strength_modified/4):
            return 2
        elif(weight < strength_modified):
            return 3
        else:
            return 4
    
    def apply_weight_penalty(self, weight_penalty, value,  parameter):
        if(weight_penalty == 0):
            return value
        elif(weight_penalty == 1):
            if(parameter == 'evasion'):
                return value - value * 0.15
            elif(parameter == 'agility'):
                return value - value * 0.15
            elif(parameter == 'hit_chance'):
                return value - value * 0.1
            else:
                return value
        elif(weight_penalty == 2):
            if(parameter == 'evasion'):
                return value - value * 0.3
            elif(parameter == 'agility'):
                return value - value * 0.3
            elif(parameter == 'hit_chance'):
                return value - value * 0.15
            elif(parameter == 'movement'):
                return value - 1
            else:
                return value
        elif(weight_penalty == 3):
            if(parameter == 'evasion'):
                return value - value * 0.6
            elif(parameter == 'agility'):
                return value - value * 0.6
            elif(parameter == 'hit_chance'):
                return value - value * 0.25
            elif(parameter == 'movement'):
                return value - 1
            else:
                return value
        elif(weight_penalty == 4):
            if(parameter == 'evasion'):
                return value - value * 0.75
            elif(parameter == 'agility'):
                return value - value * 0.75
            elif(parameter == 'hit_chance'):
                return value - value * 0.4
            elif(parameter == 'movement'):
                return value - 2
            else:
                return value
    
    def extend_unit(self, unit: UnitDTO) -> UnitDTO:
        vitality = 0
        strength = 0
        dexterity = 0
        mind = 0
        faith = 0
        essence = 0
        agility = 0
        hit_chance = 0
        evasion = 0
        armor = 0
        magic_armor = 0
        hit_rate = 0
        movement = 0
        shield = 0
        physical_damage = 0
        magical_damage = 0

        vitality = self.value_multiplier( unit.base_vitality, unit.specialization.vitality, 10 )
        strength = self.value_multiplier( unit.base_strength, unit.specialization.strength, 5 );
        dexterity = self.value_multiplier( unit.base_dexterity, unit.specialization.dexterity, 5 );
        mind = self.value_multiplier( unit.base_mind, unit.specialization.mind, 5 );
        faith = self.value_multiplier( unit.base_faith, unit.specialization.faith, 5 );

        essence = self.value_multiplier( unit.base_essence, unit.specialization.essence, 10 );
        agility = self.value_multiplier( unit.base_agility, unit.specialization.agility, 5 );
        hit_chance = self.value_multiplier( unit.base_hit_chance, unit.specialization.hit_chance, 5 );
        evasion = self.value_multiplier( unit.base_evasion, unit.specialization.evasion, 5 );

        hit_rate = unit.specialization.hit_rate
        movement = unit.specialization.movement

        # Main stats Bonuses
        vitality += faith;
        essence += mind;
        hit_chance += dexterity/2;
        evasion += dexterity/2;

        # Damage
        physical_damage = strength + dexterity;
        magical_damage = mind + faith;

        # From items
        vitality += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.vitality, acc), unit.items, 0)
        #strength += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.strength, acc), unit.items, 0)
        #dexterity += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.dexterity, acc), unit.items, 0)
        #mind += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.mind, acc), unit.items, 0)
        #faith += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.faith, acc), unit.items, 0)
        essence += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.essence, acc), unit.items, 0)
        agility += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.agility, acc), unit.items, 0)
        hit_chance += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.hit_chance, acc), unit.items, 0)
        evasion += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.evasion, acc), unit.items, 0)
        physical_damage += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.physical_damage, acc), unit.items, 0)
        magical_damage += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.magical_damage, acc), unit.items, 0)
        armor += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.armor, acc), unit.items, 0)
        magic_armor += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.magic_armor, acc), unit.items, 0)

        shield += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.shield, acc), unit.items, 0)

        weight = functools.reduce(lambda acc, item: item.item.weight*item.quantity + acc, unit.items, 0)

        # From traits
        vitality += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.vitality, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        #strength += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.strength, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        #dexterity += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.dexterity, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        #mind += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.mind, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        #faith += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.faith, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        essence += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.essence, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        agility += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.agility, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        hit_chance += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.hit_chance, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        evasion += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.evasion, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        physical_damage += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.physical_damage, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        magical_damage += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.magical_damage, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        armor += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.armor, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);
        magic_armor += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.magic_armor, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);

        shield += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.shield, acc), trait.trait.effects, 0) + acc, unit.faction.traits, 0);

        weight_penalty = self.weight_penalty(strength, weight, 1.1)

        # Apply weight penalty
        evasion = self.apply_weight_penalty(weight_penalty, evasion, 'evasion')
        agility = self.apply_weight_penalty(weight_penalty, agility, 'agility')
        movement = self.apply_weight_penalty(weight_penalty, movement, 'movement')
        hit_chance = self.apply_weight_penalty(weight_penalty, hit_chance, 'hit_chance')

        # Rounding
        vitality = round(vitality, 1)
        strength = round(strength, 1)
        dexterity = round(dexterity, 1)
        mind = round(mind, 1)
        faith = round(faith, 1)
        essence = round(essence, 1)
        agility = round(agility, 1)
        hit_chance = round(hit_chance, 1)
        evasion = round(evasion, 1)
        armor = round(armor, 1)
        magic_armor = round(magic_armor, 1)
        shield = round(shield, 1)
        physical_damage = round(physical_damage, 1)
        magical_damage = round(magical_damage, 1)
        weight = round(weight, 1)
        
        # Assigning
        unit_extended = unit.dict()

        unit_extended["vitality"] = vitality
        unit_extended["strength"] = strength
        unit_extended["dexterity"] = dexterity
        unit_extended["mind"] = mind
        unit_extended["faith"] = faith
        unit_extended["essence"] = essence
        unit_extended["agility"] = agility
        unit_extended["hit_chance"] = hit_chance
        unit_extended["evasion"] = evasion
        unit_extended["armor"] = armor
        unit_extended["magic_armor"] = magic_armor
        unit_extended["hit_rate"] = hit_rate
        unit_extended["movement"] = movement
        unit_extended["shield"] = shield
        unit_extended["physical_damage"] = physical_damage
        unit_extended["magical_damage"] = magical_damage
        unit_extended["weight"] = weight
        unit_extended["weight_penalty"] = weight_penalty

        return unit_extended


