from typing import List
from fastapi import UploadFile

from .fileService import FileService
from ..models.subFactionDTO import SubFactionRankDTO, SubFactionRankUpdateDTO, SubFactionRankCreateDTO

class SubFactionRankService:
    def __init__(self, database):
        self.database = database
        self.file_service = FileService()
    
    async def get_all(self) -> List[SubFactionRankDTO]:
        return await self.database.factionrank.find_many()
    
    async def get_by_id(self, id: str) -> SubFactionRankDTO:
        return await self.database.factionrank.find_unique(where={"id": id})

    async def get_by_faction_id(self, id: str) -> List[SubFactionRankDTO]:
        return await self.database.factionrank.find_many(
            where={ "faction_id": id },
        )
    
    async def create(self, rank: SubFactionRankCreateDTO) -> SubFactionRankDTO:
        rank = await self.database.factionrank.create( 
            data=rank.dict() 
        )

        return rank
        
    async def update(self, id: str, rank: SubFactionRankUpdateDTO) -> SubFactionRankDTO:
        rank_dict = rank.dict()

        # Get rank Data
        rank_current = await self.database.factionrank.find_unique( 
            where={"id": id} 
        )
        if(not rank_current): return None
        rank_current_dict = rank_current.dict()

        # If incomming data is empty, use current data
        for key in rank_dict:
            if rank_dict[key] is None or rank_dict[key] == "":
                rank_dict[key] = rank_current_dict[key]
        
        return await self.database.factionrank.update( 
            where={"id": id}, 
            data=rank_dict 
        )
    
    async def delete(self, id: str) -> SubFactionRankDTO:
        return await self.database.factionrank.delete(
            where={"id": id}
        )