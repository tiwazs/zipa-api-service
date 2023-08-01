from prisma import Prisma
from ..models.effectDTO import EffectDTO, EffectUpdateDTO, EffectCreateDTO
from typing import List

class EffectService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[EffectDTO]:
        return await self.database.effect.find_many()

    async def get_by_id(self, id: str) -> EffectDTO:
        return await self.database.effect.find_unique( 
            where={"id": id} 
        )

    async def create(self, effect: EffectCreateDTO) -> EffectDTO:
        return await self.database.effect.create( 
            data=effect.dict() 
        )

    async def update(self, id: str, effect: EffectDTO) -> EffectDTO:
        effect_dict = effect.dict()

        # Get effect Data
        effect_current = await self.database.effect.find_unique( 
            where={"id": id} 
        )
        if(not effect_current): return None
        effect_current_dict = effect_current.dict()

        # If incomming data is empty, use current data
        for key in effect_dict:
            if effect_dict[key] is None or effect_dict[key] == "":
                effect_dict[key] = effect_current_dict[key]
        
        return await self.database.effect.update( 
            where={"id": id}, 
            data=effect_dict 
        )

    async def delete(self, id: str) -> EffectDTO:
        return await self.database.effect.delete(
            where={"id": id}
        )