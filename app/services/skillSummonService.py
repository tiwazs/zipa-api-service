from ..models.skillSummonDTO import SkillSummonDTO, SkillSummonCreateDTO, SkillSummonUpdateDTO
from typing import List

class SkillSummonService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[SkillSummonDTO]:
        return await self.database.skillsummon.find_many()

    async def get_by_id(self, id: str) -> SkillSummonDTO:
        return await self.database.skillsummon.find_unique( 
            where={"id": id} 
        )
    
    async def update_skill_summon(self, skill_summon: SkillSummonUpdateDTO) -> SkillSummonDTO:
        skill_summon_dict = skill_summon.dict() if isinstance(skill_summon, SkillSummonUpdateDTO) else skill_summon

        # Get skill_summon Data
        skill_summon_current = await self.database.skillsummon.find_first( 
            where={"skill_id": skill_summon_dict['skill_id'], "unit_id": skill_summon_dict['unit_id']} 
        )
        if(not skill_summon_current): return None
        skill_summon_current_dict = skill_summon_current.dict()

        # If incomming data is empty, use current data
        for key in skill_summon_dict:
            if skill_summon_dict[key] is None:
                skill_summon_dict[key] = skill_summon_current_dict[key]
        
        return await self.database.skillsummon.update( 
            where={"id": skill_summon_current_dict['id']}, 
            data=skill_summon_dict 
        )
    

    async def create(self, skill_summon: SkillSummonCreateDTO) -> SkillSummonDTO:
        data = skill_summon.dict() if isinstance(skill_summon, SkillSummonCreateDTO) else skill_summon

        return await self.database.skillsummon.create( 
            data=data
        )

    async def delete(self, id: str) -> SkillSummonDTO:
        return await self.database.skillsummon.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, skill_id: str, summon_id: str) -> SkillSummonDTO:
        skill_summon = await self.database.skillsummon.find_first(
            where={"skill_id": skill_id, "unit_id": summon_id}
        )

        if skill_summon:
            return await self.database.skillsummon.delete(
                where={"id": skill_summon.id}
            )
        else:
            return None
        