from prisma import Prisma
from ..models.traitDTO import TraitDTO, TraitUpdateDTO, TraitCreateDTO
from typing import List

class TraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[TraitDTO]:
        return await self.database.trait.find_many()

    async def get_by_id(self, id: str) -> TraitDTO:
        return await self.database.trait.find_unique( 
            where={"id": id} 
        )

    async def create(self, trait: TraitCreateDTO) -> TraitDTO:
        return await self.database.trait.create( 
            data=trait.dict() 
        )

    async def update(self, id: str, trait: TraitDTO) -> TraitDTO:
        trait_dict = trait.dict()

        # Get trait Data
        trait_current = await self.database.trait.find_unique( 
            where={"id": id} 
        )
        if(not trait_current): return None
        trait_current_dict = trait_current.dict()

        # If incomming data is empty, use current data
        for key in trait_dict:
            if trait_dict[key] is None:
                trait_dict[key] = trait_current_dict[key]
        
        return await self.database.trait.update( 
            where={"id": id}, 
            data=trait_dict 
        )

    async def delete(self, id: str) -> TraitDTO:
        return await self.database.trait.delete(
            where={"id": id}
        )