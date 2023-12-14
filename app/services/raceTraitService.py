from ..models.raceTraitDTO import RaceTraitDTO, RaceTraitCreateDTO, RaceTraitUpdateDTO
from typing import List

class RaceTraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[RaceTraitDTO]:
        return await self.database.racetrait.find_many()

    async def get_by_id(self, id: str) -> RaceTraitDTO:
        return await self.database.racetrait.find_unique( 
            where={"id": id} 
        )
    
    async def update_race_trait(self, id: str, race_trait: RaceTraitUpdateDTO) -> RaceTraitDTO:
        race_trait_dict = race_trait.dict()

        # Get race_trait Data
        race_trait_current = await self.database.racetrait.find_unique( 
            where={"id": id} 
        )
        if(not race_trait_current): return None
        race_trait_current_dict = race_trait_current.dict()

        # If incomming data is empty, use current data
        for key in race_trait_dict:
            if race_trait_dict[key] is None:
                race_trait_dict[key] = race_trait_current_dict[key]
        
        return await self.database.racetrait.update( 
            where={"id": id}, 
            data=race_trait_dict 
        )
    

    async def create(self, race_trait: RaceTraitCreateDTO) -> RaceTraitDTO:
        data = race_trait.dict() if isinstance(race_trait, RaceTraitCreateDTO) else race_trait

        return await self.database.racetrait.create( 
            data=data
        )

    async def delete(self, id: str) -> RaceTraitDTO:
        return await self.database.racetrait.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, race_id: str, trait_id: str) -> RaceTraitDTO:
        race_trait = await self.database.racetrait.find_first(
            where={"race_id": race_id, "trait_id": trait_id}
        )

        if race_trait:
            return await self.database.racetrait.delete(
                where={"id": race_trait.id}
            )