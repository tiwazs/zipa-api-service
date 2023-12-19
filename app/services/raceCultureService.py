from ..models.raceDTO import RaceCultureDTO, RaceCultureCreateDTO, RaceCultureUpdateDTO
from typing import List

class RaceCultureService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[RaceCultureDTO]:
        return await self.database.raceculture.find_many()

    async def get_by_id(self, id: str) -> RaceCultureDTO:
        return await self.database.raceculture.find_unique( 
            where={"id": id} 
        )
    
    async def update_race_culture(self, id: str, race_culture: RaceCultureUpdateDTO) -> RaceCultureDTO:
        race_culture_dict = race_culture.dict()

        # Get race_culture Data
        race_culture_current = await self.database.raceculture.find_unique( 
            where={"id": id} 
        )
        if(not race_culture_current): return None
        race_culture_current_dict = race_culture_current.dict()

        # If incomming data is empty, use current data
        for key in race_culture_dict:
            if race_culture_dict[key] is None:
                race_culture_dict[key] = race_culture_current_dict[key]
        
        return await self.database.raceculture.update( 
            where={"id": id}, 
            data=race_culture_dict 
        )
    

    async def create(self, race_culture: RaceCultureCreateDTO) -> RaceCultureDTO:
        data = race_culture.dict() if isinstance(race_culture, RaceCultureCreateDTO) else race_culture

        return await self.database.raceculture.create( 
            data=data
        )

    async def delete(self, id: str) -> RaceCultureDTO:
        return await self.database.raceculture.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, race_id: str, culture_id: str) -> RaceCultureDTO:
        race_culture = await self.database.raceculture.find_first(
            where={"race_id": race_id, "culture_id": culture_id}
        )

        if race_culture:
            return await self.database.raceculture.delete(
                where={"id": race_culture.id}
            )