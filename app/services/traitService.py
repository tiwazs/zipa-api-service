from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService
from .traitEffectService import TraitEffectService
from ..models.traitDTO import TraitDTO, TraitUpdateDTO, TraitCreateDTO
from ..models.traitEffectDTO import TraitEffectCreateDTO
from typing import List

class TraitService:
    def __init__(self, database):
        self.database = database
        self.trait_effect_service = TraitEffectService(database)
        self.file_service = FileService()

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
            if trait_dict[key] is None or trait_dict[key] == "":
                trait_dict[key] = trait_current_dict[key]
        
        return await self.database.trait.update( 
            where={"id": id}, 
            data=trait_dict 
        )
    
    async def add_effect(self, trait_effect: TraitEffectCreateDTO) -> TraitDTO:
        await self.trait_effect_service.create(trait_effect)

        return await self.database.trait.find_unique( 
            where={"id": trait_effect.trait_id}, 
            include={ 
                "effects": {
                    "include": {
                        "effect": True
                    }
                }
            }
        )
    
    async def remove_effect(self, id: str, effect_id: str) -> TraitDTO:
        await self.trait_effect_service.delete_by_ids(id, effect_id)

        return await self.database.trait.find_unique( where={"id": id} )

    async def delete(self, id: str) -> TraitDTO:
        return await self.database.trait.delete(
            where={"id": id}
        )
    
    async def upload_image(self, id: str, image: UploadFile):
        trait = await self.database.trait.find_unique( 
            where={"id": id} 
        )
        if(not trait): return None

        # Save image
        filename = f"{trait.id}.jpg"
        filepath = self.file_service.save(image, "app/static/traits", filename)

        return filepath