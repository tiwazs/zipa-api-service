from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService
from .unitItemService import UnitItemService
from ..models.unitDTO import UnitDTO, UnitItemCreateDTO, UnitUpdateDTO, UnitCreateDTO
from typing import List

class UnitService:
    def __init__(self, database):
        self.database = database
        self.unit_item_service = UnitItemService(database)
        self.file_service = FileService()
    
    async def get_all(self, include_items) -> List[UnitDTO]:
        return await self.database.unit.find_many(
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            }
        )
    
    async def get_by_id(self, id: str, include_items) -> UnitDTO:
        return await self.database.unit.find_unique( 
            where={"id": id},
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            }
        )

    async def get_by_faction_id(self, id: str, include_items) -> List[UnitDTO]:
        return await self.database.unit.find_many( 
            include={
                "items": False if not include_items else {
                    "include": {
                        "item": include_items
                    }
                }
            },
            where={
                "factions": {
                    "some": {
                        "faction_id": id
                    }
                }
            }
        )
    
    async def create(self, unit: UnitCreateDTO) -> UnitDTO:
        # Get Unit Items
        unit_items = unit.items.copy() if unit.items else None
        del unit.items

        unit = await self.database.unit.create( 
            data=unit.dict() 
        )

        # Assign Unit Items
        try:
            if unit_items:
                for unit_item in unit_items:
                    await self.unit_item_service.create({"unit_specialization_id":unit.id, "item_id":unit_item.item_id, "quantity":unit_item.quantity})
        except Exception as e:
            await self.database.unit.delete(where={"id": unit.id})
            raise e
        
        return await self.database.unit.find_unique(
            where={"id": unit.id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def update(self, id: str, unit: UnitUpdateDTO) -> UnitDTO:
        unit_dict = unit.dict()

        # Get unit Data
        unit_current = await self.database.unit.find_unique( 
            where={"id": id} 
        )
        if(not unit_current): return None
        unit_current_dict = unit_current.dict()

        # If incomming data is empty, use current data
        for key in unit_dict:
            if unit_dict[key] is None or unit_dict[key] == "":
                unit_dict[key] = unit_current_dict[key]
        
        return await self.database.unit.update( 
            where={"id": id}, 
            data=unit_dict 
        )
    
    async def add_item(self, id: str, item_id: str, quantity: int) -> UnitDTO:
        await self.unit_item_service.create({"unit_specialization_id":id, "item_id":item_id, "quantity":quantity})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def remove_item(self, id: str, item_id: str) -> UnitDTO:
        await self.unit_item_service.delete_by_ids(id, item_id)

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def update_item(self, id: str, unit_item: UnitItemCreateDTO) -> UnitDTO:
        await self.unit_item_service.update({"unit_specialization_id": id, "item_id": unit_item.item_id, "quantity": unit_item.quantity})

        return await self.database.unit.find_unique(
            where={"id": id},
            include={
                "items": {
                    "include": {
                        "item": True
                    }
                }
            }
        )
    
    async def delete(self, id: str) -> UnitDTO:
        return await self.database.unit.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        unit = await self.database.unit.find_unique( 
            where={"id": id} 
        )
        if(not unit): return None

        # Save image
        filename = f"{unit.id}.jpg"
        filepath = self.file_service.save(image, "app/static/specializations", filename)

        return filepath