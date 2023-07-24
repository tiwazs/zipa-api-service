from ..models.unitSkillDTO import UnitSkillDTO, UnitSkillCreateDTO, UnitSkillUpdateDTO
from typing import List

class UnitSkillService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[UnitSkillDTO]:
        return await self.database.unitskill.find_many()

    async def get_by_id(self, id: str) -> UnitSkillDTO:
        return await self.database.unitskill.find_unique( 
            where={"id": id} 
        )
    
    async def update_unit_skill(self, id: str, unit_skill: UnitSkillUpdateDTO) -> UnitSkillDTO:
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
    

    async def create(self, unit_skill: UnitSkillCreateDTO) -> UnitSkillDTO:
        return await self.database.unitskill.create( 
            data=unit_skill.dict() 
        )

    async def delete(self, id: str) -> UnitSkillDTO:
        return await self.database.unitskill.delete(
            where={"id": id}
        )