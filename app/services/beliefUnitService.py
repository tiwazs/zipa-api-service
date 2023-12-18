from prisma import Prisma
from ..models.beliefDTO import BeliefUnitDTO, BeliefUnitCreateDTO
from typing import List

class BeliefUnitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[BeliefUnitDTO]:
        return await self.database.beliefunitspecialization.find_many()

    async def get_by_id(self, id: str) -> BeliefUnitDTO:
        return await self.database.beliefunitspecialization.find_unique( 
            where={"id": id} 
        )

    async def create(self, belief: BeliefUnitCreateDTO) -> BeliefUnitDTO:
        data = belief.dict() if isinstance(belief, BeliefUnitCreateDTO) else belief

        return await self.database.beliefunitspecialization.create( 
            data=data
        )

    async def delete(self, id: str) -> BeliefUnitDTO:
        return await self.database.beliefunitspecialization.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, belief_id: str, unit_specialization_id: str) -> BeliefUnitDTO:
        belief_unit = await self.database.beliefunitspecialization.find_first(
            where={"belief_id": belief_id, "unit_specialization_id": unit_specialization_id}
        )

        if(belief_unit):
            return await self.database.beliefunitspecialization.delete(
                where={"id": belief_unit.id}
            )