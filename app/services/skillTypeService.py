from prisma import Prisma
from ..models.skillTypeDTO import SkillTypeDTO, SkillTypeUpdateDTO, SkillTypeCreateDTO
from typing import List

class SkillTypeService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[SkillTypeDTO]:
        return await self.database.skilltype.find_many()

    async def get_by_id(self, id: str) -> SkillTypeDTO:
        return await self.database.skilltype.find_unique( 
            where={"id": id} 
        )

    async def create(self, skill_type: SkillTypeCreateDTO) -> SkillTypeDTO:
        return await self.database.skilltype.create( 
            data=skill_type.dict() 
        )

    async def update(self, id: str, skill_type: SkillTypeDTO) -> SkillTypeDTO:
        skill_type_dict = skill_type.dict()

        # Get skillType Data
        skill_type_current = await self.database.skilltype.find_unique( 
            where={"id": id} 
        )
        if(not skill_type_current): return None
        skill_type_current_dict = skill_type_current.dict()

        # If incomming data is empty, use current data
        for key in skill_type_dict:
            if skill_type_dict[key] is None:
                skill_type_dict[key] = skill_type_current_dict[key]
        
        return await self.database.skilltype.update( 
            where={"id": id}, 
            data=skill_type_dict 
        )

    async def delete(self, id: str) -> SkillTypeDTO:
        return await self.database.skilltype.delete(
            where={"id": id}
        )