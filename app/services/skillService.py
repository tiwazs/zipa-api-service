from prisma import Prisma
from ..models.skillDTO import SkillDTO, SkillUpdateDTO, SkillCreateDTO
from .assignedSkillTypeService import AssignedSkillTypeService
from typing import List

class SkillService:
    def __init__(self, database):
        self.database = database
        self.assigned_skill_type_service = AssignedSkillTypeService(database)

    async def get_all(self, include_type, include_effects) -> List[SkillDTO]:
        return await self.database.skill.find_many(
            include={ 
                "skill_types": False if not include_type else {
                    "include": {
                        "skill_type": include_type
                    }
                },
                "effects": False if not include_effects else {
                    "include": {
                        "effect": include_effects
                    }
                }
            }
        )

    async def get_by_id(self, id: str, include_type: bool, include_effects: bool) -> SkillDTO:
        return await self.database.skill.find_unique( 
            where={"id": id},
            include={ 
                "skill_types": False if not include_type else {
                    "include": {
                        "skill_type": include_type
                    }
                },
                "effects": False if not include_effects else {
                    "include": {
                        "effect": include_effects
                    }
                }
            }
        )

    async def create(self, skill: SkillCreateDTO) -> SkillDTO:
        skill_type_ids = skill.skill_type_ids.copy() if skill.skill_type_ids else None
        del skill.skill_type_ids

        # Create skill
        skill = await self.database.skill.create( 
            data=skill.dict() 
        )

        # Assign skill types
        try:
            if skill_type_ids:
                for skill_type_id in skill_type_ids:
                    print(f'creating skill type {skill_type_id}')
                    await self.assigned_skill_type_service.create({"skill_id":skill.id, "skill_type_id":skill_type_id})
        except Exception as e:
            await self.database.skill.delete(where={"id": skill.id})
            raise e
        
        return skill
    
    async def update(self, id: str, skill: SkillDTO) -> SkillDTO:
        skill_dict = skill.dict()

        # Get skill Data
        skill_current = await self.database.skill.find_unique( 
            where={"id": id} 
        )
        if(not skill_current): return None
        skill_current_dict = skill_current.dict()

        # If incomming data is empty, use current data
        for key in skill_dict:
            if skill_dict[key] is None:
                skill_dict[key] = skill_current_dict[key]
        
        return await self.database.skill.update( 
            where={"id": id}, 
            data=skill_dict 
        )

    async def add_type(self, id: str, skill_type_id: str) -> SkillDTO:
        await self.assigned_skill_type_service.create({"skill_id":id, "skill_type_id":skill_type_id})

        skill = await self.database.skill.find_unique( 
            where={"id": id},
            include={
                "skill_types": True
            }
        )
        return skill
    
    async def remove_type(self, id: str, skill_type_id: str) -> SkillDTO:
        await self.assigned_skill_type_service.delete_by_ids(id, skill_type_id)

        skill = await self.database.skill.find_unique( 
            where={"id": id},
            include={
                "skill_types": True
            }
        )
        return skill

    async def delete(self, id: str) -> SkillDTO:
        return await self.database.skill.delete(
            where={"id": id}
        )
