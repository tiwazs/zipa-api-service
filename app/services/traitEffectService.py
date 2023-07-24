from ..models.traitEffectDTO import TraitEffectDTO, TraitEffectCreateDTO
from typing import List

class TraitEffectService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[TraitEffectDTO]:
        return await self.database.traiteffect.find_many()

    async def get_by_id(self, id: str) -> TraitEffectDTO:
        return await self.database.traiteffect.find_unique( 
            where={"id": id} 
        )

    async def create(self, trait_effect: TraitEffectCreateDTO) -> TraitEffectDTO:
        # Convert DTO to dict if needed
        data = trait_effect.dict() if isinstance(trait_effect, TraitEffectCreateDTO) else trait_effect

        return await self.database.traiteffect.create( 
            data=data
        )

    async def delete(self, id: str) -> TraitEffectDTO:
        return await self.database.traiteffect.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, trait_id: str, effect_id: str) -> TraitEffectDTO:
        tait_effect = await self.database.traiteffect.find_first(
            where={"trait_id": trait_id, "effect_id": effect_id}
        )

        if tait_effect:
            return await self.database.traiteffect.delete(
                where={"id": tait_effect.id}
            )