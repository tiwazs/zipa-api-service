from ..models.itemTraitDTO import ItemTraitDTO, ItemTraitCreateDTO, ItemTraitUpdateDTO
from typing import List

class ItemTraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[ItemTraitDTO]:
        return await self.database.itemtrait.find_many()

    async def get_by_id(self, id: str) -> ItemTraitDTO:
        return await self.database.itemtrait.find_unique( 
            where={"id": id} 
        )
    
    async def update_item_trait(self, id: str, item_trait: ItemTraitUpdateDTO) -> ItemTraitDTO:
        item_trait_dict = item_trait.dict()

        # Get item_trait Data
        item_trait_current = await self.database.itemtrait.find_unique( 
            where={"id": id} 
        )
        if(not item_trait_current): return None
        item_trait_current_dict = item_trait_current.dict()

        # If incomming data is empty, use current data
        for key in item_trait_dict:
            if item_trait_dict[key] is None:
                item_trait_dict[key] = item_trait_current_dict[key]
        
        return await self.database.itemtrait.update( 
            where={"id": id}, 
            data=item_trait_dict 
        )
    

    async def create(self, item_trait: ItemTraitCreateDTO) -> ItemTraitDTO:
        data = item_trait.dict() if isinstance(item_trait, ItemTraitCreateDTO) else item_trait

        return await self.database.itemtrait.create( 
            data=data
        )

    async def delete(self, id: str) -> ItemTraitDTO:
        return await self.database.itemtrait.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, item_id: str, trait_id: str) -> ItemTraitDTO:
        item_trait = await self.database.itemtrait.find_first(
            where={"item_id": item_id, "trait_id": trait_id}
        )

        if item_trait:
            return await self.database.itemtrait.delete(
                where={"id": item_trait.id}
            )