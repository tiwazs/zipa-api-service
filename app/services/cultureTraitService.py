from ..models.cultureDTO import CultureTraitDTO, CultureTraitCreateDTO, CultureTraitUpdateDTO
from typing import List

class CultureTraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[CultureTraitDTO]:
        return await self.database.culturetrait.find_many()

    async def get_by_id(self, id: str) -> CultureTraitDTO:
        return await self.database.culturetrait.find_unique( 
            where={"id": id} 
        )
    
    async def update_culture_trait(self, id: str, culture_trait: CultureTraitUpdateDTO) -> CultureTraitDTO:
        culture_trait_dict = culture_trait.dict()

        # Get culture_trait Data
        culture_trait_current = await self.database.culturetrait.find_unique( 
            where={"id": id} 
        )
        if(not culture_trait_current): return None
        culture_trait_current_dict = culture_trait_current.dict()

        # If incomming data is empty, use current data
        for key in culture_trait_dict:
            if culture_trait_dict[key] is None:
                culture_trait_dict[key] = culture_trait_current_dict[key]
        
        return await self.database.culturetrait.update( 
            where={"id": id}, 
            data=culture_trait_dict 
        )
    

    async def create(self, culture_trait: CultureTraitCreateDTO) -> CultureTraitDTO:
        data = culture_trait.dict() if isinstance(culture_trait, CultureTraitCreateDTO) else culture_trait

        return await self.database.culturetrait.create( 
            data=data
        )

    async def delete(self, id: str) -> CultureTraitDTO:
        return await self.database.culturetrait.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, culture_id: str, trait_id: str) -> CultureTraitDTO:
        culture_trait = await self.database.culturetrait.find_first(
            where={"culture_id": culture_id, "trait_id": trait_id}
        )

        if culture_trait:
            return await self.database.culturetrait.delete(
                where={"id": culture_trait.id}
            )