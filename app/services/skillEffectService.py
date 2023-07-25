from ..models.skillEffectDTO import SkillEffectDTO, SkillEffectCreateDTO, SkillEffectUpdateDTO
from typing import List

class SkillEffectService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[SkillEffectDTO]:
        return await self.database.skilleffect.find_many()

    async def get_by_id(self, id: str) -> SkillEffectDTO:
        return await self.database.skilleffect.find_unique( 
            where={"id": id} 
        )
    
    async def update_skill_effect(self, skill_effect: SkillEffectUpdateDTO) -> SkillEffectDTO:
        skill_effect_dict = skill_effect.dict() if isinstance(skill_effect, SkillEffectUpdateDTO) else skill_effect

        # Get skill_effect Data
        skill_effect_current = await self.database.skilleffect.find_first( 
            where={"skill_id": skill_effect_dict['skill_id'], "effect_id": skill_effect_dict['effect_id']} 
        )
        if(not skill_effect_current): return None
        skill_effect_current_dict = skill_effect_current.dict()

        # If incomming data is empty, use current data
        for key in skill_effect_dict:
            if skill_effect_dict[key] is None:
                skill_effect_dict[key] = skill_effect_current_dict[key]
        
        return await self.database.skilleffect.update( 
            where={"id": skill_effect_current_dict['id']}, 
            data=skill_effect_dict 
        )
    

    async def create(self, skill_effect: SkillEffectCreateDTO) -> SkillEffectDTO:
        data = skill_effect.dict() if isinstance(skill_effect, SkillEffectCreateDTO) else skill_effect

        return await self.database.skilleffect.create( 
            data=data
        )

    async def delete(self, id: str) -> SkillEffectDTO:
        return await self.database.skilleffect.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, skill_id: str, effect_id: str) -> SkillEffectDTO:
        skill_effect = await self.database.skilleffect.find_first(
            where={"skill_id": skill_id, "effect_id": effect_id}
        )

        if skill_effect:
            return await self.database.skilleffect.delete(
                where={"id": skill_effect.id}
            )
        else:
            return None
        