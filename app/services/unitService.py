import functools
from fastapi import UploadFile
from prisma import Prisma
import re

from ..services.fileService import FileService
from .unitItemService import UnitItemService
from ..models.unitDTO import UnitDTO, UnitItemCreateDTO, UnitItemUpdateDTO, UnitUpdateDTO, UnitCreateDTO
from typing import List

class UnitService:
    def __init__(self, database):
        self.database = database
        self.unit_item_service = UnitItemService(database)
        self.file_service = FileService()
    
    async def get_all(self, include_items, include_race, include_specialization, include_culture, include_belief) -> List[UnitDTO]:
        return await self.database.unit.find_many(
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": {
                            "include":{
                                "skills": {
                                    "include":{
                                        "skill":True
                                    }
                                },
                                "traits": {
                                    "include":{
                                        "trait": {
                                            "include":{
                                                "effects": {
                                                    "include":{
                                                        "effect": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "culture": False if not include_culture else {
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
                "Belief": False if not include_belief else {
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
                "race": False if not include_race else {
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

    async def get_all_by_user(self, user_id, include_items, include_race, include_specialization, include_culture, include_belief) -> List[UnitDTO]:
        return await self.database.unit.find_many(
            where={
                "user_id": user_id
            },
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": {
                            "include":{
                                "skills": {
                                    "include":{
                                        "skill": {
                                            "include":{
                                                "effects": {
                                                    "include":{
                                                        "effect": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "traits": {
                                    "include":{
                                        "trait": {
                                            "include":{
                                                "effects": {
                                                    "include":{
                                                        "effect": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "culture": False if not include_culture else {
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
                "Belief": False if not include_belief else {
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
                "race": False if not include_race else {
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
                        },
                        "items": {
                            "include": {
                                "item": include_specialization
                            }
                        },
                        "skills": {
                            "include": {
                                "skill": {
                                    "include": {
                                        "effects": {
                                            "include": {
                                                "effect": True
                                            }
                                        }
                                    }                                          
                                }
                            }
                        },
                    }
                },
            }
        )

    async def get_by_id(self, id: str, include_items, include_race, include_specialization, include_culture, include_belief) -> UnitDTO:
        return await self.database.unit.find_unique( 
            where={"id": id},
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": {
                            "include":{
                                "skills": {
                                    "include":{
                                        "skill":True
                                    }
                                },
                                "traits": {
                                    "include":{
                                        "trait": {
                                            "include":{
                                                "effects": {
                                                    "include":{
                                                        "effect": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "culture": False if not include_culture else {
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
                "Belief": False if not include_belief else {
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
                "race": False if not include_race else {
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

    async def get_all_extended(self, include_items, include_race, include_specialization, include_culture, include_belief) -> List[UnitDTO]:
        users = await self.get_all(include_items, include_race, include_specialization, include_culture, include_belief)

        return [self.extend_unit(unit) for unit in users]
    
    async def get_all_extended_by_user(self, user_id, include_items, include_race, include_specialization, include_culture, include_belief) -> List[UnitDTO]:
        users = await self.get_all_by_user(user_id, include_items, include_race, include_specialization, include_culture, include_belief)

        return [self.extend_unit(unit) for unit in users]
    
    async def get_extended_by_id(self, id: str, include_items, include_race, include_specialization, include_culture, include_belief) -> UnitDTO:
        unit = await self.get_by_id(id, include_items, include_race, include_specialization, include_culture, include_belief)

        return self.extend_unit(unit)

    async def get_by_race_id(self, id: str, include_items) -> List[UnitDTO]:
        return await self.database.unit.find_many( 
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            },
            where={
                "races": {
                    "some": {
                        "race_id": id
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
    
    async def add_item(self, id: str, item_id: str, quantity: int, equipped: bool) -> UnitDTO:
        await self.unit_item_service.create({"unit_id":id, "item_id":item_id, "quantity":quantity, "equipped":equipped})

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
    
    async def update_item(self, id: str, item_id: str, unit_item: UnitItemUpdateDTO) -> UnitDTO:
        unit_item_dict = unit_item.dict() if isinstance(unit_item, UnitItemUpdateDTO) else unit_item
        unit_item_dict["unit_id"] = id
        unit_item_dict["item_id"] = item_id
        await self.unit_item_service.update(unit_item_dict)

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
    
    def mod_parameter_operation(self, mod_parameter_string: str, parameter: float, equipped = True):
        if mod_parameter_string is None: return 0
        regex = '(?P<sign>[+-])?(?P<value>([\d+.]+|ND|MD|HP))?(?P<porcentage>\s*%)?(?P<max>\s*max)?'
        match = re.search(regex, mod_parameter_string)
        sign = match['sign']
        max = match['max']
        value = match['value']
        porcentage = match['porcentage']

        if(not equipped): return parameter
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

    def weight_penalty(self, load_capacity: float, weight: float, strength_rate: float):
        load_capacity_modified = load_capacity * strength_rate
        if(weight < load_capacity_modified/4):
            return 0
        elif(weight < load_capacity_modified/2):
            return 1
        elif(weight < 3*load_capacity_modified/4):
            return 2
        elif(weight < load_capacity_modified):
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
    
    def apply_ascension(self, value, tier):
        if(tier == 1):
            return value*1.24
        elif(tier == 2):
            return value*1.18
        elif(tier == 3):
            return value*1.12
        elif(tier == 4):
            return value*1.05
    
    def ascension_parameters(self, parameters, tier):
        if parameters is None: parameters = ""

        if tier == 1:
            max_points = 23
            max_points_single = 7
            max_points_damage = 12
        elif tier == 2:
            max_points = 20
            max_points_single = 6
            max_points_damage = 10
        elif tier == 3:
            max_points = 17
            max_points_single = 5
            max_points_damage = 8
        else:
            max_points = 14
            max_points_single = 4
            max_points_damage = 6

        count_points = 0

        # Reading the parameters selected to increase
        regex_vitality = '(?i)(?P<VITALITY>\d+)\s*vit'
        regex_strength = '(?i)(?P<STRENGTH>\d+)\s*str'
        regex_dexterity = '(?i)(?P<DEXTERITY>\d+)\s*dex'
        regex_mind = '(?i)(?P<MIND>\d+)\s*min'
        regex_faith = '(?i)(?P<FAITH>\d+)\s*fai'
        regex_essence = '(?i)(?P<ESSENCE>\d+)\s*ess'
        regex_agility = '(?i)(?P<AGILITY>\d+)\s*agi'
        regex_hit_chance = '(?i)(?P<HIT_CHANCE>\d+)\s*hit'
        regex_evasion = '(?i)(?P<EVASION>\d+)\s*eva'
        
        ascended_parameters = {}

        match = re.search(regex_vitality, parameters)
        ascended_parameters['vitality'] = int( match['VITALITY'] ) if match else 0
        match = re.search(regex_strength, parameters)
        ascended_parameters['strength'] = int( match['STRENGTH'] ) if match else 0
        match = re.search(regex_dexterity, parameters)
        ascended_parameters['dexterity'] = int( match['DEXTERITY'] ) if match else 0
        match = re.search(regex_mind, parameters)
        ascended_parameters['mind'] = int( match['MIND'] ) if match else 0
        match = re.search(regex_faith, parameters)
        ascended_parameters['faith'] = int( match['FAITH'] ) if match else 0
        match = re.search(regex_essence, parameters)
        ascended_parameters['essence'] = int( match['ESSENCE'] ) if match else 0
        match = re.search(regex_agility, parameters)
        ascended_parameters['agility'] = int( match['AGILITY'] ) if match else 0
        match = re.search(regex_hit_chance, parameters)
        ascended_parameters['hit_chance'] = int( match['HIT_CHANCE'] ) if match else 0
        match = re.search(regex_evasion, parameters)
        ascended_parameters['evasion'] = int( match['EVASION'] ) if match else 0

        empty_parameters = {
            "vitality": 0,
            "strength": 0,
            "dexterity": 0,
            "mind": 0,
            "faith": 0,
            "essence": 0,
            "agility": 0,
            "hit_chance": 0,
            "evasion": 0
        }

        count_points = ascended_parameters['vitality'] + ascended_parameters['strength'] + ascended_parameters['dexterity'] + ascended_parameters['mind'] + ascended_parameters['faith'] + ascended_parameters['essence'] + ascended_parameters['agility'] + ascended_parameters['hit_chance'] + ascended_parameters['evasion']
        if count_points > max_points: return empty_parameters

        if ascended_parameters['strength'] + ascended_parameters['dexterity'] > max_points_damage: return empty_parameters

        for parameter in ascended_parameters.keys():
            if ascended_parameters[parameter] > max_points_single:
                return empty_parameters
        
        ascended_parameters['vitality'] = ascended_parameters["vitality"]*6
        ascended_parameters['essence'] = ascended_parameters["essence"]*6
        return ascended_parameters                        
    
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
        armor_piercing = 0
        spell_piercing = 0
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
        load_capacity = unit.specialization.load_capacity
        movement = unit.specialization.movement

        # Apply Ascention bonus
        if unit.ascended:
            ascension_parameters = self.ascension_parameters(unit.ascended_params, unit.specialization.tier)

            vitality = self.apply_ascension(vitality, unit.specialization.tier) + ascension_parameters['vitality']
            strength = self.apply_ascension(strength, unit.specialization.tier) + ascension_parameters['strength']
            dexterity = self.apply_ascension(dexterity, unit.specialization.tier) + ascension_parameters['dexterity']
            mind = self.apply_ascension(mind, unit.specialization.tier) + ascension_parameters['mind']
            faith = self.apply_ascension(faith, unit.specialization.tier) + ascension_parameters['faith']
            essence = self.apply_ascension(essence, unit.specialization.tier) + ascension_parameters['essence']
            agility = self.apply_ascension(agility, unit.specialization.tier) + ascension_parameters['agility']
            hit_chance = self.apply_ascension(hit_chance, unit.specialization.tier) + ascension_parameters['hit_chance']
            evasion = self.apply_ascension(evasion, unit.specialization.tier) + ascension_parameters['evasion']

        # Main stats Bonuses
        vitality += 0.6*faith + 0.5*strength;
        essence += 1*mind + 0.6*faith;
        hit_chance += 0.5*dexterity;
        evasion += 0.5*dexterity;

        # Damage
        physical_damage = strength + 1.2*dexterity;
        magical_damage = 1.2*mind + faith;

        # From items
        vitality += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.vitality, acc, item.equipped), unit.items, 0)
        #strength += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.strength, acc, item.equipped), unit.items, 0)
        #dexterity += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.dexterity, acc, item.equipped), unit.items, 0)
        #mind += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.mind, acc, item.equipped), unit.items, 0)
        #faith += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.faith, acc, item.equipped), unit.items, 0)
        essence += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.essence, acc, item.equipped), unit.items, 0)
        agility += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.agility, acc, item.equipped), unit.items, 0)
        hit_chance += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.hit_chance, acc, item.equipped), unit.items, 0)
        evasion += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.evasion, acc, item.equipped), unit.items, 0)
        physical_damage += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.physical_damage, acc, item.equipped), unit.items, 0)
        magical_damage += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.magical_damage, acc, item.equipped), unit.items, 0)
        armor += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.armor, acc, item.equipped), unit.items, 0)
        magic_armor += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.magic_armor, acc, item.equipped), unit.items, 0)
        armor_piercing += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.armor_piercing, acc, item.equipped), unit.items, 0)
        spell_piercing += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.spell_piercing, acc, item.equipped), unit.items, 0)

        shield += functools.reduce(lambda acc, item: self.mod_parameter_operation(item.item.shield, acc, item.equipped), unit.items, 0)

        weight = functools.reduce(lambda acc, item: item.item.weight*item.quantity + acc, unit.items, 0)

        # From traits
        vitality += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.vitality, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        #strength += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.strength, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        #dexterity += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.dexterity, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        #mind += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.mind, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        #faith += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.faith, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        essence += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.essence, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        agility += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.agility, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        hit_chance += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.hit_chance, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        evasion += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.evasion, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        physical_damage += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.physical_damage, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        magical_damage += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.magical_damage, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        armor += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.armor, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        magic_armor += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.magic_armor, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        armor_piercing += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.armor_piercing, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);
        spell_piercing += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.spell_piercing, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);

        shield += functools.reduce(lambda acc, trait: functools.reduce(lambda acc, effect: self.mod_parameter_operation(effect.effect.shield, acc), trait.trait.effects, 0) + acc, unit.race.traits, 0);

        load_capacity = load_capacity + (0.25* strength)
        weight_penalty = self.weight_penalty(load_capacity, weight, 1)

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
        unit_extended["armor_piercing"] = armor_piercing
        unit_extended["spell_piercing"] = spell_piercing
        unit_extended["hit_rate"] = hit_rate
        unit_extended["movement"] = movement
        unit_extended["shield"] = shield
        unit_extended["physical_damage"] = physical_damage
        unit_extended["magical_damage"] = magical_damage
        unit_extended["load_capacity"] = load_capacity
        unit_extended["weight"] = weight
        unit_extended["weight_penalty"] = weight_penalty

        return unit_extended


