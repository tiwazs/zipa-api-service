from prisma import Prisma
from ..models.factionDTO import FactionDTO, FactionUpdateDTO, FactionCreateDTO
from typing import List

class FactionService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[FactionDTO]:
        return await self.database.faction.find_many()

    async def get_by_id(self, id: str) -> FactionDTO:
        return await self.database.faction.find_unique( 
            where={"id": id} 
        )

    async def create(self, faction: FactionCreateDTO) -> FactionDTO:
        return await self.database.faction.create( 
            data=faction.dict() 
        )

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