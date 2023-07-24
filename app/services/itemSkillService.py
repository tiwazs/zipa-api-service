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
    
    async def update_item_skill(self, id: str, item_skill: ItemSkillUpdateDTO) -> ItemSkillDTO:
        item_skill_dict = item_skill.dict()

        # Get item_skill Data
        item_skill_current = await self.database.itemskill.find_unique( 
            where={"id": id} 
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
        return await self.database.itemskill.create( 
            data=item_skill.dict() 
        )

    async def delete(self, id: str) -> ItemSkillDTO:
        return await self.database.itemskill.delete(
            where={"id": id}
        )