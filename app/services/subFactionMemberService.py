from ..models.subFactionDTO import SubFactionMemberDTO
from typing import List

class SubFactionMemberService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[SubFactionMemberDTO]:
        return await self.database.subfactionmember.find_many()

    async def get_by_id(self, id: str) -> SubFactionMemberDTO:
        return await self.database.subfactionmember.find_unique( 
            where={"id": id} 
        )

    async def create(self, sub_faction: SubFactionMemberDTO) -> SubFactionMemberDTO:
        data = sub_faction.dict() if isinstance(sub_faction, SubFactionMemberDTO) else sub_faction

        return await self.database.subfactionmember.create( 
            data=data
        )

    async def delete(self, id: str) -> SubFactionMemberDTO:
        return await self.database.subfactionmember.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, faction_id: str, unit_id: str) -> SubFactionMemberDTO:
        faction_unit = await self.database.subfactionmember.find_first(
            where={"faction_id": faction_id, "unit_id": unit_id}
        )

        if(faction_unit):
            return await self.database.subfactionmember.delete(
                where={"id": faction_unit.id}
            )