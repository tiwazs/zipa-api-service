from prisma import Prisma
from .traitEffectService import TraitEffectService
from ..models.traitDTO import TraitDTO, TraitUpdateDTO, TraitCreateDTO
from typing import List

class TraitService:
    def __init__(self, database):
        self.database = database
        self.trait_effect_service = TraitEffectService(database)

    async def get_all(self) -> List[TraitDTO]:
        return await self.database.trait.find_many()
    
    async def get_all_ext(self) -> List[TraitDTO]:
        return await self.database.trait.find_many(
            include={ 
                "effects": {
                    "include": {
                        "effect": True
                    }
                }
            }
        )

    async def get_by_id(self, id: str) -> TraitDTO:
        return await self.database.trait.find_unique( 
            where={"id": id} 
        )
    
    async def get_by_id_ext(self, id: str) -> TraitDTO:
        return await self.database.trait.find_unique( 
            where={"id": id},
            include={ 
                "effects": {
                    "include": {
                        "effect": True
                    }
                }
            }
        )

    async def create(self, trait: TraitCreateDTO) -> TraitDTO:
        effect_ids = trait.effect_ids.copy() if trait.effect_ids else None
        del trait.effect_ids

        # Create trait
        trait = await self.database.trait.create( 
            data=trait.dict() 
        )

        # Assign trait effects
        try:
            if effect_ids:
                for effect_id in effect_ids:
                    await self.trait_effect_service.create({"trait_id":trait.id, "effect_id":effect_id})
        except Exception as e:
            await self.database.trait.delete(where={"id": trait.id})
            raise e
        
        return trait

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