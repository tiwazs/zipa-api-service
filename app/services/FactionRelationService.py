from ..models.FactionDTO import FactionRelationDTO
from typing import List

class FactionRelationService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[FactionRelationDTO]:
        return await self.database.factionrelation.find_many()

    async def get_by_id(self, id: str) -> FactionRelationDTO:
        return await self.database.factionrelation.find_unique( 
            where={"id": id} 
        )    

    async def create(self, relation: FactionRelationDTO) -> FactionRelationDTO:
        data = relation.dict() if isinstance(relation, FactionRelationDTO) else relation

        return await self.database.factionrelation.create( 
            data=data
        )

    async def delete(self, id: str) -> FactionRelationDTO:
        return await self.database.factionrelation.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, faction_id: str, faction2_id: str) -> FactionRelationDTO:
        faction_trait = await self.database.factionrelation.find_first(
            where={"faction_id": faction_id, "faction2_id": faction2_id}
        )

        if faction_trait:
            return await self.database.factionrelation.delete(
                where={"id": faction_trait.id}
            )