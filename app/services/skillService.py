from prisma import Prisma
from ..models.skillDTO import SkillDTO, SkillUpdateDTO, SkillCreateDTO
from typing import List

class SkillService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[SkillDTO]:
        return await self.database.skill.find_many()

    async def get_by_id(self, id: str) -> SkillDTO:
        return await self.database.skill.find_unique( 
            where={"id": id} 
        )

    async def create(self, skill: SkillCreateDTO) -> SkillDTO:
        return await self.database.skill.create( 
            data=skill.dict() 
        )

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

    async def delete(self, id: str) -> SkillDTO:
        return await self.database.skill.delete(
            where={"id": id}
        )
