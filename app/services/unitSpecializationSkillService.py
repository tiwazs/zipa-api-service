from ..models.unitSpecializationSkillDTO import UnitSpecializationSkillDTO, UnitSpecializationSkillCreateDTO, UnitSpecializationSkillUpdateDTO
from typing import List

class UnitSpecializationSkillService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[UnitSpecializationSkillDTO]:
        return await self.database.unitskill.find_many()

    async def get_by_id(self, id: str) -> UnitSpecializationSkillDTO:
        return await self.database.unitskill.find_unique( 
            where={"id": id} 
        )
    
    async def update_unit_skill(self, id: str, unit_skill: UnitSpecializationSkillUpdateDTO) -> UnitSpecializationSkillDTO:
        unit_skill_dict = unit_skill.dict()

        # Get unit_skill Data
        unit_skill_current = await self.database.unitskill.find_unique( 
            where={"id": id} 
        )
        if(not unit_skill_current): return None
        unit_skill_current_dict = unit_skill_current.dict()

        # If incomming data is empty, use current data
        for key in unit_skill_dict:
            if unit_skill_dict[key] is None:
                unit_skill_dict[key] = unit_skill_current_dict[key]
        
        return await self.database.unitskill.update( 
            where={"id": id}, 
            data=unit_skill_dict 
        )
    

    async def create(self, unit_skill: UnitSpecializationSkillCreateDTO) -> UnitSpecializationSkillDTO:
        data = unit_skill.dict() if isinstance(unit_skill, UnitSpecializationSkillCreateDTO) else unit_skill

        return await self.database.unitskill.create( 
            data=data
        )

    async def delete(self, id: str) -> UnitSpecializationSkillDTO:
        return await self.database.unitskill.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, unit_specialization_id: str, skill_id: str) -> UnitSpecializationSkillDTO:
        unit_skill = await self.database.unitskill.find_first(
            where={"unit_specialization_id": unit_specialization_id, "skill_id": skill_id}
        )

        if unit_skill:
            return await self.database.unitskill.delete(
                where={"id": unit_skill.id}
            )