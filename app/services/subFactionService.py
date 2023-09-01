from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService
from ..services.subFactionMemberService import SubFactionMemberService
from ..models.subFactionDTO import SubFactionDTO, SubFactionUpdateDTO, SubFactionCreateDTO, SubFactionMemberDTO
from typing import List

class SubFactionService:
    def __init__(self, database):
        self.database = database
        self.sub_faction_unit_service = SubFactionMemberService(database)
        self.file_service = FileService()

    async def get_all(self, include_ranks: bool, include_units: bool) -> List[SubFactionDTO]:
        return await self.database.subfaction.find_many(
            include={
                "members": False if not include_units else {
                    "include": {
                        "unit": include_units
                    }
                },
                "faction_ranks": include_ranks
            }
        )

    async def get_by_id(self, id: str, include_ranks: bool, include_units: bool) -> SubFactionDTO:
        return await self.database.subfaction.find_unique( 
            where={"id": id},
            include={
                "members": False if not include_units else {
                    "include": {
                        "unit": include_units
                    }
                },
                "faction_ranks": include_ranks
            }
        )

    async def create(self, sub_faction: SubFactionCreateDTO) -> SubFactionDTO:

        # Create sub_faction
        sub_faction = await self.database.subfaction.create( 
            data=sub_faction.dict() 
        )
        
        return await self.get_by_id(sub_faction.id, True, True)

    async def update(self, id: str, sub_faction: SubFactionUpdateDTO) -> SubFactionDTO:
        faction_dict = sub_faction.dict()

        # Get sub_faction Data
        faction_current = await self.database.subfaction.find_unique( 
            where={"id": id} 
        )
        if(not faction_current): return None
        faction_current_dict = faction_current.dict()

        # If incomming data is empty, use current data
        for key in faction_dict:
            if faction_dict[key] is None or faction_dict[key] == "":
                faction_dict[key] = faction_current_dict[key]
        
        return await self.database.subfaction.update( 
            where={"id": id}, 
            data=faction_dict 
        )
    
    async def add_unit(self, member: SubFactionMemberDTO) -> SubFactionDTO:
        sub_faction = await self.get_by_id(member.faction_id, True, True)
        if(not sub_faction): return None

        # Assign units
        await self.sub_faction_unit_service.create(member)

        return await self.get_by_id(sub_faction.id, True, True)
    
    async def remove_unit(self, id: str, unit_id: str) -> SubFactionDTO:
        sub_faction = await self.get_by_id(id, True, True)
        if(not sub_faction): return None

        # Remove units
        await self.sub_faction_unit_service.delete_by_ids(sub_faction.id, unit_id)

        return await self.get_by_id(sub_faction.id, True, True)

    async def delete(self, id: str) -> SubFactionDTO:
        return await self.database.subfaction.delete(
            where={"id": id}
        )
        
    async def upload_image(self, id: str, image: UploadFile):
        sub_faction = await self.database.subfaction.find_unique( 
            where={"id": id} 
        )
        if(not sub_faction): return None

        # Save image
        filename = f"{sub_faction.id}.jpg"
        filepath = self.file_service.save(image, "app/static/subfactions", filename)

        return filepath