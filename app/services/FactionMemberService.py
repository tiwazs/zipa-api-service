from ..models.FactionDTO import FactionMemberDTO
from typing import List

class FactionMemberService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[FactionMemberDTO]:
        return await self.database.factionmember.find_many()

    async def get_by_id(self, id: str) -> FactionMemberDTO:
        return await self.database.factionmember.find_unique( 
            where={"id": id} 
        )

    async def create(self, faction: FactionMemberDTO) -> FactionMemberDTO:
        data = faction.dict() if isinstance(faction, FactionMemberDTO) else faction

        return await self.database.factionmember.create( 
            data=data
        )

    async def delete(self, id: str) -> FactionMemberDTO:
        return await self.database.factionmember.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, faction_id: str, unit_id: str) -> FactionMemberDTO:
        faction_unit = await self.database.factionmember.find_first(
            where={"faction_id": faction_id, "unit_id": unit_id}
        )

        if(faction_unit):
            return await self.database.factionmember.delete(
                where={"id": faction_unit.id}
            )