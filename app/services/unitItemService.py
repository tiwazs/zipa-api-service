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
    
    async def update_unit_item(self, id: str, unit_item: UnitItemUpdateDTO) -> UnitItemDTO:
        unit_item_dict = unit_item.dict()

        # Get unit_item Data
        unit_item_current = await self.database.unititem.find_unique( 
            where={"id": id} 
        )
        if(not unit_item_current): return None
        unit_item_current_dict = unit_item_current.dict()

        # If incomming data is empty, use current data
        for key in unit_item_dict:
            if unit_item_dict[key] is None:
                unit_item_dict[key] = unit_item_current_dict[key]
        
        return await self.database.unititem.update( 
            where={"id": id}, 
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