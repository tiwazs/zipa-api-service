from fastapi import UploadFile
from prisma import Prisma

from .fileService import FileService
from ..models.raceGroupDTO import RaceGroupDTO, RaceGroupUpdateDTO, RaceGroupCreateDTO
from typing import List

class RaceGroupService:
    def __init__(self, database):
        self.database = database
        self.file_service = FileService()

    async def get_all(self) -> List[RaceGroupDTO]:
        return await self.database.racegroup.find_many()

    async def get_by_id(self, id: str) -> RaceGroupDTO:
        return await self.database.racegroup.find_unique( 
            where={"id": id}
        )

    async def create(self, race_group: RaceGroupCreateDTO) -> RaceGroupDTO:
        # Create race_group
        return await self.database.racegroup.create( 
            data=race_group.dict() 
        )

    async def update(self, id: str, race_group: RaceGroupDTO) -> RaceGroupDTO:
        race_group_dict = race_group.dict()

        # Get race_group Data
        race_group_current = await self.database.racegroup.find_unique( 
            where={"id": id} 
        )
        if(not race_group_current): return None
        race_group_current_dict = race_group_current.dict()

        # If incomming data is empty, use current data
        for key in race_group_dict:
            if race_group_dict[key] is None or race_group_dict[key] == "":
                race_group_dict[key] = race_group_current_dict[key]
        
        return await self.database.racegroup.update( 
            where={"id": id}, 
            data=race_group_dict 
        )
    
    async def delete(self, id: str) -> RaceGroupDTO:
        return await self.database.race_group.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        race_group = await self.database.race_group.find_unique( 
            where={"id": id} 
        )
        if(not race_group): return None

        # Save image
        filename = f"{race_group.id}.jpg"
        filepath = self.file_service.save(image, "app/static/race_groups", filename)

        return filepath