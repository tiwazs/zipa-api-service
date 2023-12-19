from ..models.raceDTO import RaceBeliefDTO, RaceBeliefCreateDTO, RaceBeliefUpdateDTO
from typing import List

class RaceBeliefService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[RaceBeliefDTO]:
        return await self.database.racebelief.find_many()

    async def get_by_id(self, id: str) -> RaceBeliefDTO:
        return await self.database.racebelief.find_unique( 
            where={"id": id} 
        )
    
    async def update_race_belief(self, id: str, race_belief: RaceBeliefUpdateDTO) -> RaceBeliefDTO:
        race_belief_dict = race_belief.dict()

        # Get race_belief Data
        race_belief_current = await self.database.racebelief.find_unique( 
            where={"id": id} 
        )
        if(not race_belief_current): return None
        race_belief_current_dict = race_belief_current.dict()

        # If incomming data is empty, use current data
        for key in race_belief_dict:
            if race_belief_dict[key] is None:
                race_belief_dict[key] = race_belief_current_dict[key]
        
        return await self.database.racebelief.update( 
            where={"id": id}, 
            data=race_belief_dict 
        )
    

    async def create(self, race_belief: RaceBeliefCreateDTO) -> RaceBeliefDTO:
        data = race_belief.dict() if isinstance(race_belief, RaceBeliefCreateDTO) else race_belief

        return await self.database.racebelief.create( 
            data=data
        )

    async def delete(self, id: str) -> RaceBeliefDTO:
        return await self.database.racebelief.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, race_id: str, belief_id: str) -> RaceBeliefDTO:
        race_belief = await self.database.racebelief.find_first(
            where={"race_id": race_id, "belief_id": belief_id}
        )

        if race_belief:
            return await self.database.racebelief.delete(
                where={"id": race_belief.id}
            )