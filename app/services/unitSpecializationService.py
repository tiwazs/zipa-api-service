from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService
from .unitSpecializationItemService import UnitSpecializationItemService
from .unitSpecializationSkillService import UnitSpecializationSkillService
from .unitSpecializationTraitService import UnitSpecializationTraitService
from ..models.unitSpecializationDTO import UnitSpecializationDTO, UnitSpecializationItemCreateDTO, UnitSpecializationUpdateDTO, UnitSpecializationCreateDTO
from typing import List

class UnitSpecializationService:
    def __init__(self, database):
        self.database = database
        self.unit_trait_service = UnitSpecializationTraitService(database)
        self.unit_skill_service = UnitSpecializationSkillService(database)
        self.unit_item_service = UnitSpecializationItemService(database)
        self.file_service = FileService()
    
    async def get_all(self, include_traits, include_skills, include_items) -> List[UnitSpecializationDTO]:
        return await self.database.unitspecialization.find_many(
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
    
    async def get_by_id(self, id: str, include_traits, include_skills, include_items) -> UnitSpecializationDTO:
        return await self.database.unitspecialization.find_unique( 
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

    async def get_by_faction_id(self, id: str, include_traits, include_skills, include_items) -> List[UnitSpecializationDTO]:
        return await self.database.unitspecialization.find_many( 
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
            },
            where={
                "factions": {
                    "some": {
                        "faction_id": id
                    }
                }
            }
        )
    
    async def create(self, unitspecialization: UnitSpecializationCreateDTO) -> UnitSpecializationDTO:
        # Get UnitSpecialization Trait ids
        unit_trait_ids = unitspecialization.trait_ids.copy() if unitspecialization.trait_ids else None
        del unitspecialization.trait_ids

        # Get UnitSpecialization Skill ids
        unit_skill_ids = unitspecialization.skill_ids.copy() if unitspecialization.skill_ids else None
        del unitspecialization.skill_ids

        # Get UnitSpecialization Items
        unit_items = unitspecialization.items.copy() if unitspecialization.items else None
        del unitspecialization.items

        unitspecialization = await self.database.unitspecialization.create( 
            data=unitspecialization.dict() 
        )

        # Assign UnitSpecialization Traits
        try:
            if unit_trait_ids:
                for unit_trait_id in unit_trait_ids:
                    await self.unit_trait_service.create({"unit_specialization_id":unitspecialization.id, "trait_id":unit_trait_id})
        except Exception as e:
            await self.database.unitspecialization.delete(where={"id": unitspecialization.id})
            raise e
        
        # Assign UnitSpecialization Skills
        try:
            if unit_skill_ids:
                for unit_skill_id in unit_skill_ids:
                    await self.unit_skill_service.create({"unit_specialization_id":unitspecialization.id, "skill_id":unit_skill_id})
        except Exception as e:
            await self.database.unitspecialization.delete(where={"id": unitspecialization.id})
            raise e
        
        # Assign UnitSpecialization Items
        try:
            if unit_items:
                for unit_item in unit_items:
                    await self.unit_item_service.create({"unit_specialization_id":unitspecialization.id, "item_id":unit_item.item_id, "quantity":unit_item.quantity})
        except Exception as e:
            await self.database.unitspecialization.delete(where={"id": unitspecialization.id})
            raise e
        
        return await self.database.unitspecialization.find_unique(
            where={"id": unitspecialization.id},
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
    
    async def update(self, id: str, unitspecialization: UnitSpecializationUpdateDTO) -> UnitSpecializationDTO:
        unit_dict = unitspecialization.dict()

        # Get unitspecialization Data
        unit_current = await self.database.unitspecialization.find_unique( 
            where={"id": id} 
        )
        if(not unit_current): return None
        unit_current_dict = unit_current.dict()

        # If incomming data is empty, use current data
        for key in unit_dict:
            if unit_dict[key] is None or unit_dict[key] == "":
                unit_dict[key] = unit_current_dict[key]
        
        return await self.database.unitspecialization.update( 
            where={"id": id}, 
            data=unit_dict 
        )
    
    async def add_trait(self, id: str, trait_id: str) -> UnitSpecializationDTO:
        await self.unit_trait_service.create({"unit_specialization_id":id, "trait_id":trait_id})

        return await self.database.unitspecialization.find_unique(
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

    async def remove_trait(self, id: str, trait_id: str) -> UnitSpecializationDTO:
        await self.unit_trait_service.delete_by_ids(id, trait_id)

        return await self.database.unitspecialization.find_unique(
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
    
    async def add_skill(self, id: str, skill_id: str) -> UnitSpecializationDTO:
        await self.unit_skill_service.create({"unit_specialization_id":id, "skill_id":skill_id})

        return await self.database.unitspecialization.find_unique(
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
    
    async def remove_skill(self, id: str, skill_id: str) -> UnitSpecializationDTO:
        await self.unit_skill_service.delete_by_ids(id, skill_id)

        return await self.database.unitspecialization.find_unique(
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
    
    async def add_item(self, id: str, item_id: str, quantity: int) -> UnitSpecializationDTO:
        await self.unit_item_service.create({"unit_specialization_id":id, "item_id":item_id, "quantity":quantity})

        return await self.database.unitspecialization.find_unique(
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
    
    async def remove_item(self, id: str, item_id: str) -> UnitSpecializationDTO:
        await self.unit_item_service.delete_by_ids(id, item_id)

        return await self.database.unitspecialization.find_unique(
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
    
    async def update_item(self, id: str, unit_item: UnitSpecializationItemCreateDTO) -> UnitSpecializationDTO:
        await self.unit_item_service.update({"unit_specialization_id": id, "item_id": unit_item.item_id, "quantity": unit_item.quantity})

        return await self.database.unitspecialization.find_unique(
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
    
    async def delete(self, id: str) -> UnitSpecializationDTO:
        return await self.database.unitspecialization.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        unitspecialization = await self.database.unitspecialization.find_unique( 
            where={"id": id} 
        )
        if(not unitspecialization): return None

        # Save image
        filename = f"{unitspecialization.id}.jpg"
        filepath = self.file_service.save(image, "app/static/specializations", filename)

        return filepath