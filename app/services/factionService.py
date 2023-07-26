from prisma import Prisma

from ..services.factionUnitService import FactionUnitService
from ..models.factionDTO import FactionDTO, FactionUpdateDTO, FactionCreateDTO
from typing import List

class FactionService:
    def __init__(self, database):
        self.database = database
        self.faction_unit_service = FactionUnitService(database)

    async def get_all(self, include_units: bool) -> List[FactionDTO]:
        return await self.database.faction.find_many(
            include={
                "units": False if not include_units else {
                    "include": {
                        "unit": include_units
                    }
                }
            }
        )

    async def get_by_id(self, id: str, include_units: bool) -> FactionDTO:
        return await self.database.faction.find_unique( 
            where={"id": id},
            include={
                "units": False if not include_units else {
                    "include": {
                        "unit": include_units
                    }
                }
            }
        )

    async def create(self, faction: FactionCreateDTO) -> FactionDTO:
        units_ids = faction.unit_ids.copy() if faction.unit_ids else None
        del faction.unit_ids

        # Create faction
        faction = await self.database.faction.create( 
            data=faction.dict() 
        )

        # Assign units
        try:
            if units_ids:
                for unit_id in units_ids:
                    await self.faction_unit_service.create({"faction_id":faction.id, "unit_id":unit_id})
        except Exception as e:
            await self.database.faction.delete(where={"id": faction.id})
            raise e
        
        return await self.get_by_id(faction.id, True)

    async def update(self, id: str, faction: FactionDTO) -> FactionDTO:
        faction_dict = faction.dict()

        # Get faction Data
        faction_current = await self.database.faction.find_unique( 
            where={"id": id} 
        )
        if(not faction_current): return None
        faction_current_dict = faction_current.dict()

        # If incomming data is empty, use current data
        for key in faction_dict:
            if faction_dict[key] is None:
                faction_dict[key] = faction_current_dict[key]
        
        return await self.database.faction.update( 
            where={"id": id}, 
            data=faction_dict 
        )

    async def delete(self, id: str) -> FactionDTO:
        return await self.database.faction.delete(
            where={"id": id}
        )