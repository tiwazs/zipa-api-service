from fastapi import UploadFile
from prisma import Prisma

from .fileService import FileService
from .cultureUnitService import CultureUnitService
from .cultureTraitService import CultureTraitService
from ..models.cultureDTO import CultureDTO, CultureUpdateDTO, CultureCreateDTO
from typing import List

class CultureService:
    def __init__(self, database):
        self.database = database
        self.culture_unit_service = CultureUnitService(database)
        self.culture_trait_service = CultureTraitService(database)
        self.file_service = FileService()

    async def get_all(self, include_traits: bool, include_units: bool) -> List[CultureDTO]:
        return await self.database.culture.find_many(
            include={
                "available_specializations": False if not include_units else {
                    "include": {
                        "unit_specialization": include_units
                    }
                },
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                }
            }
        )

    async def get_by_id(self, id: str, include_traits: bool, include_units: bool) -> CultureDTO:
        return await self.database.culture.find_unique( 
            where={"id": id},
            include={
                "available_specializations": False if not include_units else {
                    "include": {
                        "unit_specialization": include_units
                    }
                },
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                }
            }
        )

    async def create(self, culture: CultureCreateDTO) -> CultureDTO:
        units_ids = culture.unit_specialization_ids.copy() if culture.unit_specialization_ids else None
        del culture.unit_specialization_ids

        # Create culture
        culture = await self.database.culture.create( 
            data=culture.dict() 
        )

        # Assign units
        try:
            if units_ids:
                for unit_specialization_id in units_ids:
                    await self.culture_unit_service.create({"culture_id":culture.id, "unit_specialization_id":unit_specialization_id})
        except Exception as e:
            await self.database.culture.delete(where={"id": culture.id})
            raise e
        
        return await self.get_by_id(culture.id, True, True)

    async def update(self, id: str, culture: CultureDTO) -> CultureDTO:
        culture_dict = culture.dict()

        # Get culture Data
        culture_current = await self.database.culture.find_unique( 
            where={"id": id} 
        )
        if(not culture_current): return None
        culture_current_dict = culture_current.dict()

        # If incomming data is empty, use current data
        for key in culture_dict:
            if culture_dict[key] is None or culture_dict[key] == "":
                culture_dict[key] = culture_current_dict[key]
        
        return await self.database.culture.update( 
            where={"id": id}, 
            data=culture_dict 
        )
    
    async def add_trait(self, id: str, trait_id: str) -> CultureDTO:
        await self.culture_trait_service.create({"culture_id":id, "trait_id":trait_id})

        return await self.database.culture.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )

    async def remove_trait(self, id: str, trait_id: str) -> CultureDTO:
        await self.culture_trait_service.delete_by_ids(id, trait_id)

        return await self.database.culture.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )
    
    async def add_unit(self, id: str, unit_specialization_id: str) -> CultureDTO:
        culture = await self.get_by_id(id, True, True)
        if(not culture): return None

        # Assign unit_specializations
        await self.culture_unit_service.create({"culture_id":culture.id, "unit_specialization_id":unit_specialization_id})

        return await self.get_by_id(culture.id, True, True)
    
    async def remove_unit(self, id: str, unit_specialization_id: str) -> CultureDTO:
        culture = await self.get_by_id(id, True, True)
        if(not culture): return None

        # Remove unit_specializations
        await self.culture_unit_service.delete_by_ids(culture.id, unit_specialization_id)

        return await self.get_by_id(culture.id, True, True)

    async def delete(self, id: str) -> CultureDTO:
        return await self.database.culture.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        culture = await self.database.culture.find_unique( 
            where={"id": id} 
        )
        if(not culture): return None

        # Save image
        filename = f"{culture.id}.jpg"
        filepath = self.file_service.save(image, "app/static/cultures", filename)

        return filepath