from ..models.beliefDTO import BeliefTraitDTO, BeliefTraitCreateDTO, BeliefTraitUpdateDTO
from typing import List

class BeliefTraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[BeliefTraitDTO]:
        return await self.database.belieftrait.find_many()

    async def get_by_id(self, id: str) -> BeliefTraitDTO:
        return await self.database.belieftrait.find_unique( 
            where={"id": id} 
        )
    
    async def update_belief_trait(self, id: str, belief_trait: BeliefTraitUpdateDTO) -> BeliefTraitDTO:
        belief_trait_dict = belief_trait.dict()

        # Get belief_trait Data
        belief_trait_current = await self.database.belieftrait.find_unique( 
            where={"id": id} 
        )
        if(not belief_trait_current): return None
        belief_trait_current_dict = belief_trait_current.dict()

        # If incomming data is empty, use current data
        for key in belief_trait_dict:
            if belief_trait_dict[key] is None:
                belief_trait_dict[key] = belief_trait_current_dict[key]
        
        return await self.database.belieftrait.update( 
            where={"id": id}, 
            data=belief_trait_dict 
        )
    

    async def create(self, belief_trait: BeliefTraitCreateDTO) -> BeliefTraitDTO:
        data = belief_trait.dict() if isinstance(belief_trait, BeliefTraitCreateDTO) else belief_trait

        return await self.database.belieftrait.create( 
            data=data
        )

    async def delete(self, id: str) -> BeliefTraitDTO:
        return await self.database.belieftrait.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, belief_id: str, trait_id: str) -> BeliefTraitDTO:
        belief_trait = await self.database.belieftrait.find_first(
            where={"belief_id": belief_id, "trait_id": trait_id}
        )

        if belief_trait:
            return await self.database.belieftrait.delete(
                where={"id": belief_trait.id}
            )