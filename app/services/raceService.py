from fastapi import UploadFile
from prisma import Prisma

from .fileService import FileService
from .raceUnitService import RaceUnitService
from .raceTraitService import RaceTraitService
from .raceCultureService import RaceCultureService
from .raceBeliefService import RaceBeliefService
from ..models.raceDTO import RaceDTO, RaceUpdateDTO, RaceCreateDTO
from typing import List

class RaceService:
    def __init__(self, database):
        self.database = database
        self.race_unit_service = RaceUnitService(database)
        self.race_trait_service = RaceTraitService(database)
        self.race_culture_service = RaceCultureService(database)
        self.race_belief_service = RaceBeliefService(database)
        self.file_service = FileService()

    async def get_all(self, include_traits: bool,  include_cultures: bool,  include_beliefs: bool, include_units: bool) -> List[RaceDTO]:
        return await self.database.race.find_many(
            include={
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                },
                "available_cultures": False if not include_cultures else {
                    "include": {
                        "culture": include_cultures
                    }
                },
                "available_beliefs": False if not include_beliefs else {
                    "include": {
                        "belief": include_beliefs
                    }
                },
            }
        )

    async def get_by_id(self, id: str, include_traits: bool, include_cultures: bool,  include_beliefs: bool, include_units: bool) -> RaceDTO:
        return await self.database.race.find_unique( 
            where={"id": id},
            include={
                "traits": False if not include_traits else {
                    "include": {
                        "trait": include_traits
                    }
                },
                "available_cultures": False if not include_cultures else {
                    "include": {
                        "culture": include_cultures
                    }
                },
                "available_beliefs": False if not include_beliefs else {
                    "include": {
                        "belief": include_beliefs
                    }
                },
            }
        )

    async def create(self, race: RaceCreateDTO) -> RaceDTO:
        units_ids = race.unit_specialization_ids.copy() if race.unit_specialization_ids else None
        del race.unit_specialization_ids

        # Create race
        race = await self.database.race.create( 
            data=race.dict() 
        )

        # Assign units
        try:
            if units_ids:
                for unit_specialization_id in units_ids:
                    await self.race_unit_service.create({"race_id":race.id, "unit_specialization_id":unit_specialization_id})
        except Exception as e:
            await self.database.race.delete(where={"id": race.id})
            raise e
        
        return await self.get_by_id(race.id, True, True, True, True)

    async def update(self, id: str, race: RaceDTO) -> RaceDTO:
        race_dict = race.dict()

        # Get race Data
        race_current = await self.database.race.find_unique( 
            where={"id": id} 
        )
        if(not race_current): return None
        race_current_dict = race_current.dict()

        # If incomming data is empty, use current data
        for key in race_dict:
            if race_dict[key] is None or race_dict[key] == "":
                race_dict[key] = race_current_dict[key]
        
        return await self.database.race.update( 
            where={"id": id}, 
            data=race_dict 
        )
    
    async def add_trait(self, id: str, trait_id: str) -> RaceDTO:
        await self.race_trait_service.create({"race_id":id, "trait_id":trait_id})

        return await self.database.race.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )

    async def remove_trait(self, id: str, trait_id: str) -> RaceDTO:
        await self.race_trait_service.delete_by_ids(id, trait_id)

        return await self.database.race.find_unique(
            where={"id": id},
            include={
                "traits": {
                    "include": {
                        "trait": True
                    }
                }
            }
        )
    
    async def add_unit(self, id: str, unit_specialization_id: str) -> RaceDTO:
        race = await self.get_by_id(id, True, True, True, True)
        if(not race): return None

        # Assign unit_specializations
        await self.race_unit_service.create({"race_id":race.id, "unit_specialization_id":unit_specialization_id})

        return await self.get_by_id(race.id, True, True, True, True)
    
    async def remove_unit(self, id: str, unit_specialization_id: str) -> RaceDTO:
        race = await self.get_by_id(id, True, True, True, True)
        if(not race): return None

        # Remove unit_specializations
        await self.race_unit_service.delete_by_ids(race.id, unit_specialization_id)

        return await self.get_by_id(race.id, True, True, True, True)

    async def add_culture(self, id: str, culture_id: str) -> RaceDTO:
        await self.race_culture_service.create({"race_id":id, "culture_id":culture_id})

        return await self.database.race.find_unique(
            where={"id": id},
            include={
                "available_cultures": {
                    "include": {
                        "culture": True
                    }
                }
            }
        )

    async def remove_culture(self, id: str, culture_id: str) -> RaceDTO:
        await self.race_culture_service.delete_by_ids(id, culture_id)

        return await self.database.race.find_unique(
            where={"id": id},
            include={
                "available_cultures": {
                    "include": {
                        "culture": True
                    }
                }
            }
        )

    async def add_belief(self, id: str, belief_id: str) -> RaceDTO:
        await self.race_belief_service.create({"race_id":id, "belief_id":belief_id})

        return await self.database.race.find_unique(
            where={"id": id},
            include={
                "available_beliefs": {
                    "include": {
                        "belief": True
                    }
                }
            }
        )

    async def remove_belief(self, id: str, belief_id: str) -> RaceDTO:
        await self.race_belief_service.delete_by_ids(id, belief_id)

        return await self.database.race.find_unique(
            where={"id": id},
            include={
                "available_beliefs": {
                    "include": {
                        "belief": True
                    }
                }
            }
        )
    
    async def delete(self, id: str) -> RaceDTO:
        return await self.database.race.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        race = await self.database.race.find_unique( 
            where={"id": id} 
        )
        if(not race): return None

        # Save image
        filename = f"{race.id}.jpg"
        filepath = self.file_service.save(image, "app/static/races", filename)

        return filepath