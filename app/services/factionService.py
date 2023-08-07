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
                "unit_specializations": False if not include_units else {
                    "include": {
                        "unit_specialization": include_units
                    }
                }
            }
        )

    async def get_by_id(self, id: str, include_units: bool) -> FactionDTO:
        return await self.database.faction.find_unique( 
            where={"id": id},
            include={
                "unit_specializations": False if not include_units else {
                    "include": {
                        "unit_specialization": include_units
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
                for unit_specialization_id in units_ids:
                    await self.faction_unit_service.create({"faction_id":faction.id, "unit_specialization_id":unit_specialization_id})
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
            if faction_dict[key] is None or faction_dict[key] == "":
                faction_dict[key] = faction_current_dict[key]
        
        return await self.database.faction.update( 
            where={"id": id}, 
            data=faction_dict 
        )
    
    async def add_unit(self, id: str, unit_specialization_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True)
        if(not faction): return None

        # Assign unit_specializations
        await self.faction_unit_service.create({"faction_id":faction.id, "unit_specialization_id":unit_specialization_id})

        return await self.get_by_id(faction.id, True)
    
    async def remove_unit(self, id: str, unit_specialization_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True)
        if(not faction): return None

        # Remove unit_specializations
        await self.faction_unit_service.delete_by_ids(faction.id, unit_specialization_id)

        return await self.get_by_id(faction.id, True)

    async def delete(self, id: str) -> FactionDTO:
        return await self.database.faction.delete(
            where={"id": id}
        )