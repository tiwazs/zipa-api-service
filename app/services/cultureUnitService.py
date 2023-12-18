from prisma import Prisma
from ..models.cultureDTO import CultureUnitDTO, CultureUnitCreateDTO
from typing import List

class CultureUnitService:
    def __init__(self, database):
        self.database = database

    async def get_all(self) -> List[CultureUnitDTO]:
        return await self.database.cultureunitspecialization.find_many()

    async def get_by_id(self, id: str) -> CultureUnitDTO:
        return await self.database.cultureunitspecialization.find_unique( 
            where={"id": id} 
        )

    async def create(self, culture: CultureUnitCreateDTO) -> CultureUnitDTO:
        data = culture.dict() if isinstance(culture, CultureUnitCreateDTO) else culture

        return await self.database.cultureunitspecialization.create( 
            data=data
        )

    async def delete(self, id: str) -> CultureUnitDTO:
        return await self.database.cultureunitspecialization.delete(
            where={"id": id}
        )
    
    async def delete_by_ids(self, culture_id: str, unit_specialization_id: str) -> CultureUnitDTO:
        culture_unit = await self.database.cultureunitspecialization.find_first(
            where={"culture_id": culture_id, "unit_specialization_id": unit_specialization_id}
        )

        if(culture_unit):
            return await self.database.cultureunitspecialization.delete(
                where={"id": culture_unit.id}
            )