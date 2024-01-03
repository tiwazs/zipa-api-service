from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService

from ..models.itemDTO import ItemDTO, ItemUpdateDTO, ItemCreateDTO
from ..models.itemSkillDTO import ItemSkillCreateDTO
from ..services.itemSkillService import ItemSkillService
from ..services.itemTraitService import ItemTraitService
from typing import List

class ItemService:
    def __init__(self, database):
        self.database = database
        self.item_skill_service = ItemSkillService(database)
        self.item_trait_service = ItemTraitService(database)
        self.file_service = FileService()

    async def get_all(self, include_skills: bool, include_traits: bool, by_type: str, by_rarity: str) -> List[ItemDTO]:
        conditions = {}
        if by_type: conditions["object_type"] = by_type
        if by_rarity: conditions["rarity"] = by_rarity

        return await self.database.item.find_many(
            where=conditions,
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
                }
            }
        )

    async def get_by_id(self, id: str, include_skills: bool, include_traits: bool) -> ItemDTO:
        return await self.database.item.find_unique( 
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
                }
            }
        )

    async def create(self, item: ItemCreateDTO) -> ItemDTO:
        # Get item skills
        item_skills = item.skills.copy() if item.skills else None
        del item.skills

        # Create Item

        item = await self.database.item.create( 
            data=item.dict() 
        )

        # Assign item skills
        try:
            if item_skills:
                for item_skill in item_skills:
                    await self.item_skill_service.create({"item_id":item.id, "skill_id":item_skill.skill_id, "essence_cost":item_skill.essence_cost, "cooldown":item_skill.cooldown})
        except Exception as e:
            await self.database.item.delete(where={"id": item.id})
            raise e
        
        return await self.database.item.find_unique(
            where={"id": item.id},
            include={
                "skills": {
                    "include": {
                        "skill": True
                    }
                }
            }
        )

    async def update(self, id: str, item: ItemDTO) -> ItemDTO:
        item_dict = item.dict()

        # Get item Data
        item_current = await self.database.item.find_unique( 
            where={"id": id} 
        )
        if(not item_current): return None
        item_current_dict = item_current.dict()

        # If incomming data is empty, use current data
        for key in item_dict:
            if item_dict[key] is None or item_dict[key] == "":
                item_dict[key] = item_current_dict[key]
        
        return await self.database.item.update( 
            where={"id": id}, 
            data=item_dict 
        )
    
    async def add_skill(self, item_skill: ItemSkillCreateDTO) -> ItemDTO:
        await self.item_skill_service.create(item_skill)

        item = await self.database.item.find_unique( 
            where={"id": item_skill.item_id},
            include={
                "skills": {
                    "include": {
                        "skill": True
                    }
                }
            }
        )
        return item

    async def remove_skill(self, id: str, skill_id: str) -> ItemDTO:
        await self.item_skill_service.delete_by_ids(id, skill_id)

        item = await self.database.item.find_unique( 
            where={"id": id},
            include={
                "skills": {
                    "include": {
                        "skill": True
                    }
                }
            }
        )
        return item

    async def update_skill(self, item_skill: ItemSkillCreateDTO) -> ItemDTO:
        await self.item_skill_service.update_item_skill(item_skill)

        item = await self.database.item.find_unique( 
            where={"id": item_skill.item_id},
            include={
                "skills": {
                    "include": {
                        "skill": True
                    }
                }
            }
        )
        return item

    async def add_trait(self, id: str, trait_id: str) -> ItemDTO:
        await self.item_trait_service.create({"item_id":id, "trait_id":trait_id})

        return await self.database.item.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )

    async def remove_trait(self, id: str, trait_id: str) -> ItemDTO:
        await self.item_trait_service.delete_by_ids(id, trait_id)

        return await self.database.item.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )

    async def delete(self, id: str) -> ItemDTO:
        return await self.database.item.delete(
            where={"id": id}
        )

    async def upload_image(self, id: str, image: UploadFile):
        item = await self.database.item.find_unique( 
            where={"id": id} 
        )
        if(not item): return None

        # Save image
        filename = f"{item.id}.jpg"
        filepath = self.file_service.save(image, "app/static/items", filename)

        return filepath