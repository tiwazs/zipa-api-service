from prisma import Prisma
from ..models.factionDTO import FactionDTO, FactionUpdateDTO, FactionCreateDTO
from typing import List

class FactionService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[FactionDTO]:
        return await self.database.faction.find_many()

    async def get_by_id(self, id: str) -> FactionDTO:
        return await self.database.faction.find_unique( where={"id": id} )

    async def create(self, faction: FactionCreateDTO) -> FactionDTO:
        return await self.database.faction.create( data=faction.dict() )

    async def update(self, id: str, faction: FactionDTO) -> FactionDTO:
        return await self.database.faction.update({"id": id}, faction)

    async def delete(self, id: str) -> FactionDTO:
        return await self.database.faction.delete({"id": id})