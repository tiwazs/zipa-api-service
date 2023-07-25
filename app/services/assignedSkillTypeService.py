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
        data = assigned_skill_type.dict() if isinstance(assigned_skill_type, AssignedSkillTypeCreateDTO) else assigned_skill_type

        return await self.database.assignedskilltype.create( 
            data=data
        )

    async def delete(self, id: str) -> AssignedSkillTypeDTO:
        return await self.database.assignedskilltype.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, skill_id: str, skill_type_id: str) -> AssignedSkillTypeDTO:
        assigned_skill_type = await self.database.assignedskilltype.find_first(
            where={"skill_id": skill_id, "skill_type_id": skill_type_id}
        )

        if assigned_skill_type:
            return await self.database.assignedskilltype.delete(
                where={"id": assigned_skill_type.id}
            )