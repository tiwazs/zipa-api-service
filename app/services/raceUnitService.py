from prisma import Prisma
from ..models.raceUnitDTO import RaceUnitDTO, RaceUnitUpdateDTO, RaceUnitCreateDTO
from typing import List

class RaceUnitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[RaceUnitDTO]:
        return await self.database.raceunitspecialization.find_many()

    async def get_by_id(self, id: str) -> RaceUnitDTO:
        return await self.database.raceunitspecialization.find_unique( 
            where={"id": id} 
        )

    async def create(self, race: RaceUnitCreateDTO) -> RaceUnitDTO:
        data = race.dict() if isinstance(race, RaceUnitCreateDTO) else race

        return await self.database.raceunitspecialization.create( 
            data=data
        )

    async def delete(self, id: str) -> RaceUnitDTO:
        return await self.database.raceunitspecialization.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, race_id: str, unit_specialization_id: str) -> RaceUnitDTO:
        race_unit = await self.database.raceunitspecialization.find_first(
            where={"race_id": race_id, "unit_specialization_id": unit_specialization_id}
        )

        if(race_unit):
            return await self.database.raceunitspecialization.delete(
                where={"id": race_unit.id}
            )