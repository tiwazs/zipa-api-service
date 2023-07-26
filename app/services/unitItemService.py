from ..models.unitItemDTO import UnitItemDTO, UnitItemCreateDTO, UnitItemUpdateDTO
from typing import List

class UnitItemService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[UnitItemDTO]:
        return await self.database.unititem.find_many()

    async def get_by_id(self, id: str) -> UnitItemDTO:
        return await self.database.unititem.find_unique( 
            where={"id": id} 
        )
    
    async def update(self, unit_item: UnitItemUpdateDTO) -> UnitItemDTO:
        unit_item_dict = unit_item.dict() if isinstance(unit_item, UnitItemUpdateDTO) else unit_item

        # Get unit_item Data
        unit_item_current = await self.database.unititem.find_first( 
            where={"unit_id": unit_item_dict["unit_id"], "item_id": unit_item_dict["item_id"]}
        )
        if(not unit_item_current): return None
        unit_item_current_dict = unit_item_current.dict()

        # If incomming data is empty, use current data
        for key in unit_item_dict:
            if unit_item_dict[key] is None:
                unit_item_dict[key] = unit_item_current_dict[key]
        
        return await self.database.unititem.update( 
            where={"id": unit_item_current_dict["id"]}, 
            data=unit_item_dict 
        )
    

    async def create(self, unit_item: UnitItemCreateDTO) -> UnitItemDTO:
        data = unit_item.dict() if isinstance(unit_item, UnitItemCreateDTO) else unit_item

        return await self.database.unititem.create( 
            data=data
        )

    async def delete(self, id: str) -> UnitItemDTO:
        return await self.database.unititem.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, unit_id: str, item_id: str) -> UnitItemDTO:
        unit_item = await self.database.unititem.find_first(
            where={"unit_id": unit_id, "item_id": item_id}
        )

        if unit_item:
            return await self.database.unititem.delete(
                where={"id": unit_item.id}
            )