from ..models.unitSpecializationTraitDTO import UnitSpecializationTraitDTO, UnitSpecializationTraitCreateDTO, UnitSpecializationTraitUpdateDTO
from typing import List

class UnitSpecializationTraitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[UnitSpecializationTraitDTO]:
        return await self.database.unittrait.find_many()

    async def get_by_id(self, id: str) -> UnitSpecializationTraitDTO:
        return await self.database.unittrait.find_unique( 
            where={"id": id} 
        )
    
    async def update_unit_trait(self, id: str, unit_trait: UnitSpecializationTraitUpdateDTO) -> UnitSpecializationTraitDTO:
        unit_trait_dict = unit_trait.dict()

        # Get unit_trait Data
        unit_trait_current = await self.database.unittrait.find_unique( 
            where={"id": id} 
        )
        if(not unit_trait_current): return None
        unit_trait_current_dict = unit_trait_current.dict()

        # If incomming data is empty, use current data
        for key in unit_trait_dict:
            if unit_trait_dict[key] is None:
                unit_trait_dict[key] = unit_trait_current_dict[key]
        
        return await self.database.unittrait.update( 
            where={"id": id}, 
            data=unit_trait_dict 
        )
    

    async def create(self, unit_trait: UnitSpecializationTraitCreateDTO) -> UnitSpecializationTraitDTO:
        data = unit_trait.dict() if isinstance(unit_trait, UnitSpecializationTraitCreateDTO) else unit_trait

        return await self.database.unittrait.create( 
            data=data
        )

    async def delete(self, id: str) -> UnitSpecializationTraitDTO:
        return await self.database.unittrait.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, unit_specialization_id: str, trait_id: str) -> UnitSpecializationTraitDTO:
        unit_trait = await self.database.unittrait.find_first(
            where={"unit_specialization_id": unit_specialization_id, "trait_id": trait_id}
        )

        if unit_trait:
            return await self.database.unittrait.delete(
                where={"id": unit_trait.id}
            )