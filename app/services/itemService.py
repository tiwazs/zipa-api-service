from prisma import Prisma
from ..models.itemDTO import ItemDTO, ItemUpdateDTO, ItemCreateDTO
from typing import List

class ItemService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[ItemDTO]:
        return await self.database.item.find_many()

    async def get_by_id(self, id: str) -> ItemDTO:
        return await self.database.item.find_unique( 
            where={"id": id} 
        )

    async def create(self, item: ItemCreateDTO) -> ItemDTO:
        return await self.database.item.create( 
            data=item.dict() 
        )

    async def update(self, id: str, item: ItemDTO) -> ItemDTO:
        item_dict = item.dict()

        # Get item Data
        item_current = await self.database.item.find_unique( 
            where={"id": id} 
        )
        if(not item_current): return None
        item_current_dict = item_current.dict()

        # If incomming data is empty, use current data
        for key in item_dict:
            if item_dict[key] is None:
                item_dict[key] = item_current_dict[key]
        
        return await self.database.item.update( 
            where={"id": id}, 
            data=item_dict 
        )

    async def delete(self, id: str) -> ItemDTO:
        return await self.database.item.delete(
            where={"id": id}
        )