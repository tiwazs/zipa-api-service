from prisma import Prisma
from ..services.unitItemService import UnitItemService
from ..services.unitSkillService import UnitSkillService
from ..services.unitTraitService import UnitTraitService
from ..models.unitDTO import UnitDTO, UnitItemCreateDTO, UnitUpdateDTO, UnitCreateDTO
from typing import List

class UnitService:
    def __init__(self, database):
        self.database = database
        self.unit_trait_service = UnitTraitService(database)
        self.unit_skill_service = UnitSkillService(database)
        self.unit_item_service = UnitItemService(database)
    
    async def get_all(self, include_traits, include_skills, include_items) -> List[UnitDTO]:
        return await self.database.unit.find_many(
            include={
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                },
                "skills": False if not include_skills else {
                    "include": {
                        "skill": include_skills
                    }
                },
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            }
        )
    
    async def get_by_id(self, id: str, include_traits, include_skills, include_items) -> UnitDTO:
        return await self.database.unit.find_unique( 
            where={"id": id},
                        include={
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                },
                "skills": False if not include_skills else {
                    "include": {
                        "skill": include_skills
                    }
                },
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            }
        )

    async def get_by_faction_id(self, id: str, include_traits, include_skills, include_items) -> List[UnitDTO]:
        return await self.database.unit.find_many( 
            where={"faction_id": id},
                        include={
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                },
                "skills": False if not include_skills else {
                    "include": {
                        "skill": include_skills
                    }
                },
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            }
        )
    
    async def create(self, unit: UnitCreateDTO) -> UnitDTO:
        # Get Unit Trait ids
        unit_trait_ids = unit.trait_ids.copy() if unit.trait_ids else None
        del unit.trait_ids

        # Get Unit Skill ids
        unit_skill_ids = unit.skill_ids.copy() if unit.skill_ids else None
        del unit.skill_ids

        # Get Unit Items
        unit_items = unit.items.copy() if unit.items else None
        del unit.items

        unit = await self.database.unit.create( 
            data=unit.dict() 
        )

        # Assign Unit Traits
        try:
            if unit_trait_ids:
                for unit_trait_id in unit_trait_ids:
                    await self.unit_trait_service.create({"unit_id":unit.id, "trait_id":unit_trait_id})
        except Exception as e:
            await self.database.unit.delete(where={"id": unit.id})
            raise e
        
        # Assign Unit Skills
        try:
            if unit_skill_ids:
                for unit_skill_id in unit_skill_ids:
                    await self.unit_skill_service.create({"unit_id":unit.id, "skill_id":unit_skill_id})
        except Exception as e:
            await self.database.unit.delete(where={"id": unit.id})
            raise e
        
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
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
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
            if unit_dict[key] is None:
                unit_dict[key] = unit_current_dict[key]
        
        return await self.database.unit.update( 
            where={"id": id}, 
            data=unit_dict 
        )
    
    async def add_trait(self, id: str, trait_id: str) -> UnitDTO:
        await self.unit_trait_service.create({"unit_id":id, "trait_id":trait_id})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )

    async def remove_trait(self, id: str, trait_id: str) -> UnitDTO:
        await self.unit_trait_service.delete_by_ids(id, trait_id)

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def add_skill(self, id: str, skill_id: str) -> UnitDTO:
        await self.unit_skill_service.create({"unit_id":id, "skill_id":skill_id})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def remove_skill(self, id: str, skill_id: str) -> UnitDTO:
        await self.unit_skill_service.delete_by_ids(id, skill_id)

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def add_item(self, id: str, item_id: str, quantity: int) -> UnitDTO:
        await self.unit_item_service.create({"unit_id":id, "item_id":item_id, "quantity":quantity})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
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
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
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
                "traits": {
                    "include": {
                        "trait": True
                    }
                },
                "skills": {
                    "include": {
                        "skill": True
                    }
                },
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