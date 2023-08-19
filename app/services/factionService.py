from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService
from ..services.factionUnitService import FactionUnitService
from ..services.factionTraitService import FactionTraitService
from ..models.factionDTO import FactionDTO, FactionUpdateDTO, FactionCreateDTO
from typing import List

class FactionService:
    def __init__(self, database):
        self.database = database
        self.faction_unit_service = FactionUnitService(database)
        self.faction_trait_service = FactionTraitService(database)
        self.file_service = FileService()

    async def get_all(self, include_traits: bool, include_units: bool) -> List[FactionDTO]:
        return await self.database.faction.find_many(
            include={
                "unit_specializations": False if not include_units else {
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

    async def get_by_id(self, id: str, include_traits: bool, include_units: bool) -> FactionDTO:
        return await self.database.faction.find_unique( 
            where={"id": id},
            include={
                "unit_specializations": False if not include_units else {
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

    async def create(self, faction: FactionCreateDTO) -> FactionDTO:
        units_ids = faction.unit_specialization_ids.copy() if faction.unit_specialization_ids else None
        del faction.unit_specialization_ids

        # Create faction
        faction = await self.database.faction.create( 
            data=faction.dict() 
        )

        # Assign units
        try:
            if units_ids:
                for unit_specialization_id in units_ids:
                    await self.faction_unit_service.create({"faction_id":faction.id, "unit_specialization_id":unit_specialization_id})
        except Exception as e:
            await self.database.faction.delete(where={"id": faction.id})
            raise e
        
        return await self.get_by_id(faction.id, True)

    async def update(self, id: str, faction: FactionDTO) -> FactionDTO:
        faction_dict = faction.dict()

        # Get faction Data
        faction_current = await self.database.faction.find_unique( 
            where={"id": id} 
        )
        if(not faction_current): return None
        faction_current_dict = faction_current.dict()

        # If incomming data is empty, use current data
        for key in faction_dict:
            if faction_dict[key] is None or faction_dict[key] == "":
                faction_dict[key] = faction_current_dict[key]
        
        return await self.database.faction.update( 
            where={"id": id}, 
            data=faction_dict 
        )
    
    async def add_trait(self, id: str, trait_id: str) -> FactionDTO:
        await self.faction_trait_service.create({"faction_id":id, "trait_id":trait_id})

        return await self.database.faction.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )

    async def remove_trait(self, id: str, trait_id: str) -> FactionDTO:
        await self.faction_trait_service.delete_by_ids(id, trait_id)

        return await self.database.faction.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )
    
    async def add_unit(self, id: str, unit_specialization_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True)
        if(not faction): return None

        # Assign unit_specializations
        await self.faction_unit_service.create({"faction_id":faction.id, "unit_specialization_id":unit_specialization_id})

        return await self.get_by_id(faction.id, True)
    
    async def remove_unit(self, id: str, unit_specialization_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True)
        if(not faction): return None

        # Remove unit_specializations
        await self.faction_unit_service.delete_by_ids(faction.id, unit_specialization_id)

        return await self.get_by_id(faction.id, True)

    async def delete(self, id: str) -> FactionDTO:
        return await self.database.faction.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        faction = await self.database.faction.find_unique( 
            where={"id": id} 
        )
        if(not faction): return None

        # Save image
        filename = f"{faction.id}.jpg"
        filepath = self.file_service.save(image, "app/static/factions", filename)

        return filepath