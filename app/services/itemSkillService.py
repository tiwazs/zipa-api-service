from ..models.itemSkillDTO import ItemSkillDTO, ItemSkillCreateDTO, ItemSkillUpdateDTO
from typing import List

class ItemSkillService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[ItemSkillDTO]:
        return await self.database.itemskill.find_many()

    async def get_by_id(self, id: str) -> ItemSkillDTO:
        return await self.database.itemskill.find_unique( 
            where={"id": id} 
        )
    
    async def update_item_skill(self, item_skill: ItemSkillUpdateDTO) -> ItemSkillDTO:
        item_skill_dict = item_skill.dict() if isinstance(item_skill, ItemSkillUpdateDTO) else item_skill

        # Get item_skill Data
        item_skill_current = await self.database.itemskill.find_unique( 
            where={"item_id": item_skill_dict['item_id'], "skill_id": item_skill_dict['skill_id']}
        )
        if(not item_skill_current): return None
        item_skill_current_dict = item_skill_current.dict()

        # If incomming data is empty, use current data
        for key in item_skill_dict:
            if item_skill_dict[key] is None:
                item_skill_dict[key] = item_skill_current_dict[key]
        
        return await self.database.itemskill.update( 
            where={"id": id}, 
            data=item_skill_dict 
        )
    

    async def create(self, item_skill: ItemSkillCreateDTO) -> ItemSkillDTO:
        data = item_skill.dict() if isinstance(item_skill, ItemSkillCreateDTO) else item_skill

        return await self.database.itemskill.create( 
            data=data
        )

    async def delete(self, id: str) -> ItemSkillDTO:
        return await self.database.itemskill.delete(
            where={"id": id}
        )

    async def delete_by_ids(self, item_id: str, skill_id: str) -> ItemSkillDTO:
        item_skill = await self.database.itemskill.find_first(
            where={"item_id": item_id, "skill_id": skill_id}
        )

        if item_skill:
            return await self.database.itemskill.delete(
                where={"id": item_skill.id}
            )
        else:
            return None