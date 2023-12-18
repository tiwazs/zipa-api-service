from fastapi import UploadFile
from prisma import Prisma

from .fileService import FileService
from .beliefUnitService import BeliefUnitService
from .beliefTraitService import BeliefTraitService
from ..models.beliefDTO import BeliefDTO, BeliefUpdateDTO, BeliefCreateDTO
from typing import List

class BeliefService:
    def __init__(self, database):
        self.database = database
        self.belief_unit_service = BeliefUnitService(database)
        self.belief_trait_service = BeliefTraitService(database)
        self.file_service = FileService()

    async def get_all(self, include_traits: bool, include_units: bool) -> List[BeliefDTO]:
        return await self.database.belief.find_many(
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

    async def get_by_id(self, id: str, include_traits: bool, include_units: bool) -> BeliefDTO:
        return await self.database.belief.find_unique( 
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

    async def create(self, belief: BeliefCreateDTO) -> BeliefDTO:
        units_ids = belief.unit_specialization_ids.copy() if belief.unit_specialization_ids else None
        del belief.unit_specialization_ids

        # Create belief
        belief = await self.database.belief.create( 
            data=belief.dict() 
        )

        # Assign units
        try:
            if units_ids:
                for unit_specialization_id in units_ids:
                    await self.belief_unit_service.create({"belief_id":belief.id, "unit_specialization_id":unit_specialization_id})
        except Exception as e:
            await self.database.belief.delete(where={"id": belief.id})
            raise e
        
        return await self.get_by_id(belief.id, True, True)

    async def update(self, id: str, belief: BeliefDTO) -> BeliefDTO:
        belief_dict = belief.dict()

        # Get belief Data
        belief_current = await self.database.belief.find_unique( 
            where={"id": id} 
        )
        if(not belief_current): return None
        belief_current_dict = belief_current.dict()

        # If incomming data is empty, use current data
        for key in belief_dict:
            if belief_dict[key] is None or belief_dict[key] == "":
                belief_dict[key] = belief_current_dict[key]
        
        return await self.database.belief.update( 
            where={"id": id}, 
            data=belief_dict 
        )
    
    async def add_trait(self, id: str, trait_id: str) -> BeliefDTO:
        await self.belief_trait_service.create({"belief_id":id, "trait_id":trait_id})

        return await self.database.belief.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )

    async def remove_trait(self, id: str, trait_id: str) -> BeliefDTO:
        await self.belief_trait_service.delete_by_ids(id, trait_id)

        return await self.database.belief.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )
    
    async def add_unit(self, id: str, unit_specialization_id: str) -> BeliefDTO:
        belief = await self.get_by_id(id, True, True)
        if(not belief): return None

        # Assign unit_specializations
        await self.belief_unit_service.create({"belief_id":belief.id, "unit_specialization_id":unit_specialization_id})

        return await self.get_by_id(belief.id, True, True)
    
    async def remove_unit(self, id: str, unit_specialization_id: str) -> BeliefDTO:
        belief = await self.get_by_id(id, True, True)
        if(not belief): return None

        # Remove unit_specializations
        await self.belief_unit_service.delete_by_ids(belief.id, unit_specialization_id)

        return await self.get_by_id(belief.id, True, True)

    async def delete(self, id: str) -> BeliefDTO:
        return await self.database.belief.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        belief = await self.database.belief.find_unique( 
            where={"id": id} 
        )
        if(not belief): return None

        # Save image
        filename = f"{belief.id}.jpg"
        filepath = self.file_service.save(image, "app/static/beliefs", filename)

        return filepath