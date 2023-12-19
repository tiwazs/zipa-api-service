from fastapi import UploadFile
from prisma import Prisma

from .fileService import FileService
from .factionMemberService import FactionMemberService
from .factionRankService import FactionRankService
from .factionRelationService import FactionRelationService
from ..models.factionDTO import FactionDTO, FactionRankCreateDTO, FactionUpdateDTO, FactionCreateDTO, FactionMemberDTO
from typing import List

class FactionService:
    def __init__(self, database):
        self.database = database
        self.faction_rank_service = FactionRankService(database)
        self.faction_unit_service = FactionMemberService(database)
        self.faction_relation_service = FactionRelationService(database)
        self.file_service = FileService()

    async def get_all(self, include_ranks: bool, include_units: bool,  include_vassal_subjects:bool, include_overlord:bool, only_overlords:bool) -> List[FactionDTO]:
        return await self.database.faction.find_many(
            where={
                "NOT": {
                    "factions_relations2": {
                        "some": {
                            "OR": [
                                {"type": "SUBJECT"},
                                {"type": "VASSAL"}
                            ]
                        }
                    }
                }
                } if only_overlords else {},
            include={
                "members": False if not include_units else {
                    "include": {
                        "unit": include_units,
                        "faction_rank": include_units
                    }
                },
                "faction_ranks": include_ranks,
                "factions_relations": False if not include_vassal_subjects else {
                    "include": {
                        "faction2": include_vassal_subjects,
                    },
                    "where": {
                        'OR': [ {"type": "SUBJECT" },{"type": "VASSAL" } ]
                    }
                },
                "factions_relations2": False if not include_overlord else {
                    "include": {
                        "faction": include_overlord
                    },
                    "where": {
                        'OR': [ {"type": "SUBJECT" },{"type": "VASSAL" } ]
                    }
                },
            }
        )

    async def get_by_id(self, id: str, include_ranks: bool, include_units: bool,  include_vassal_subjects:bool, include_overlord:bool) -> FactionDTO:
        return await self.database.faction.find_unique( 
            where={"id": id},
            include={
                "members": False if not include_units else {
                    "include": {
                        "unit": include_units,
                        "faction_rank": include_units
                    }
                },
                "faction_ranks": include_ranks,
                "factions_relations": False if not include_vassal_subjects else {
                    "include": {
                        "faction2": include_vassal_subjects,
                    },
                    "where": {
                        'OR': [ {"type": "SUBJECT" },{"type": "VASSAL" } ]
                    }
                },
                "factions_relations2": False if not include_overlord else {
                    "include": {
                        "faction": include_overlord
                    },
                    "where": {
                        'OR': [ {"type": "SUBJECT" },{"type": "VASSAL" } ]
                    }
                },
            }
        )

    async def create(self, faction: FactionCreateDTO) -> FactionDTO:

        # Create faction
        faction = await self.database.faction.create( 
            data=faction.dict() 
        )
        
        return await self.get_by_id(faction.id, True, True, True, True)

    async def update(self, id: str, faction: FactionUpdateDTO) -> FactionDTO:
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
    
    async def add_rank(self, rank: FactionRankCreateDTO) -> FactionDTO:
        faction = await self.get_by_id(rank.faction_id, True, True, True, True)
        if(not faction): return None

        # Assign Ranks
        await self.faction_rank_service.create(rank)

        return await self.get_by_id(faction.id, True, True, True, True)
    
    async def delete_rank(self, id, rank_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True, True, True, True)
        if(not faction): return None

        # Remove Ranks
        await self.faction_rank_service.delete(rank_id)

        return await self.get_by_id(faction.id, True, True, True, True)
    
    async def add_unit(self, member: FactionMemberDTO) -> FactionDTO:
        faction = await self.get_by_id(member.faction_id, True, True, True, True)
        if(not faction): return None

        # Assign units
        await self.faction_unit_service.create(member)

        return await self.get_by_id(faction.id, True, True, True, True)
    
    async def remove_unit(self, id: str, unit_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True, True, True, True)
        if(not faction): return None

        # Remove units
        await self.faction_unit_service.delete_by_ids(faction.id, unit_id)

        return await self.get_by_id(faction.id, True, True, True, True)

    async def add_relation(self, relation: FactionRankCreateDTO) -> FactionDTO:
        faction = await self.get_by_id(relation.faction_id, True, True, True, True)
        if(not faction): return None

        faction2 = await self.get_by_id(relation.faction2_id, True, True, True, True)
        if(not faction2): return None

        # Assign Relations
        await self.faction_relation_service.create(relation)

        return await self.get_by_id(faction.id, True, True, True, True)
    
    async def delete_relation(self, faction_id, faction2_id: str) -> FactionDTO:
        faction = await self.get_by_id(id, True, True, True, True)
        if(not faction): return None

        faction2 = await self.get_by_id(id, True, True, True, True)
        if(not faction2): return None

        # Remove Relations
        await self.faction_relation_service.delete_by_ids(faction_id, faction2_id)

        return await self.get_by_id(faction.id, True, True, True, True)

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