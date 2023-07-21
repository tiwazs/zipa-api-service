from prisma import Prisma
from ..models.unitDTO import UnitDTO, UnitUpdateDTO, UnitCreateDTO
from typing import List

class UnitService:
    def __init__(self, database):
        self.database = database
    
    async def get_all(self) -> List[UnitDTO]:
        return await self.database.unit.find_many()
    
    async def get_by_id(self, id: str) -> UnitDTO:
        return await self.database.unit.find_unique( 
            where={"id": id} 
        )

    async def get_by_faction_id(self, id: str) -> List[UnitDTO]:
        return await self.database.unit.find_many( 
            where={"faction_id": id} 
        )
    
    async def create(self, unit: UnitCreateDTO) -> UnitDTO:
        return await self.database.unit.create( 
            data=unit.dict() 
        )
    
    async def update(self, id: str, unit: UnitUpdateDTO) -> UnitDTO:
        unit_dict = unit.dict()

        # Get unit Data
        unit_current = await self.database.unit.find_unique( 
            where={"id": id} 
        )
        if(not unit_current): return None
        unit_current_dict = unit_current.dict()

        # If incomming data is empty, use current data
        for key in unit_dict:
            if unit_dict[key] is None:
                unit_dict[key] = unit_current_dict[key]
        
        return await self.database.unit.update( 
            where={"id": id}, 
            data=unit_dict 
        )
    
    async def delete(self, id: str) -> UnitDTO:
        return await self.database.unit.delete(
            where={"id": id}
        )