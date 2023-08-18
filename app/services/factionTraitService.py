from ..models.factionTraitDTO import FactionTraitDTO, FactionTraitCreateDTO, FactionTraitUpdateDTO
from typing import List

class FactionTraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[FactionTraitDTO]:
        return await self.database.factiontrait.find_many()

    async def get_by_id(self, id: str) -> FactionTraitDTO:
        return await self.database.factiontrait.find_unique( 
            where={"id": id} 
        )
    
    async def update_faction_trait(self, id: str, faction_trait: FactionTraitUpdateDTO) -> FactionTraitDTO:
        faction_trait_dict = faction_trait.dict()

        # Get faction_trait Data
        faction_trait_current = await self.database.factiontrait.find_unique( 
            where={"id": id} 
        )
        if(not faction_trait_current): return None
        faction_trait_current_dict = faction_trait_current.dict()

        # If incomming data is empty, use current data
        for key in faction_trait_dict:
            if faction_trait_dict[key] is None:
                faction_trait_dict[key] = faction_trait_current_dict[key]
        
        return await self.database.factiontrait.update( 
            where={"id": id}, 
            data=faction_trait_dict 
        )
    

    async def create(self, faction_trait: FactionTraitCreateDTO) -> FactionTraitDTO:
        data = faction_trait.dict() if isinstance(faction_trait, FactionTraitCreateDTO) else faction_trait

        return await self.database.factiontrait.create( 
            data=data
        )

    async def delete(self, id: str) -> FactionTraitDTO:
        return await self.database.factiontrait.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, faction_id: str, trait_id: str) -> FactionTraitDTO:
        faction_trait = await self.database.factiontrait.find_first(
            where={"faction_id": faction_id, "trait_id": trait_id}
        )

        if faction_trait:
            return await self.database.factiontrait.delete(
                where={"id": faction_trait.id}
            )