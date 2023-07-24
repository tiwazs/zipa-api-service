from ..models.assignedSkillTypeDTO import AssignedSkillTypeDTO, AssignedSkillTypeCreateDTO
from typing import List

class AssignedSkillTypeService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[AssignedSkillTypeDTO]:
        return await self.database.assignedskilltype.find_many()

    async def get_by_id(self, id: str) -> AssignedSkillTypeDTO:
        return await self.database.assignedskilltype.find_unique( 
            where={"id": id} 
        )

    async def create(self, assigned_skill_type: AssignedSkillTypeCreateDTO) -> AssignedSkillTypeDTO:
        return await self.database.assignedskilltype.create( 
            data=assigned_skill_type.dict() 
        )

    async def delete(self, id: str) -> AssignedSkillTypeDTO:
        return await self.database.assignedskilltype.delete(
            where={"id": id}
        )