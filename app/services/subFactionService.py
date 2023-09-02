from fastapi import UploadFile
from prisma import Prisma

from ..services.fileService import FileService
from ..services.subFactionMemberService import SubFactionMemberService
from ..services.subFactionRankService import SubFactionRankService
from ..services.subFactionRelationService import SubFactionRelationService
from ..models.subFactionDTO import SubFactionDTO, SubFactionRankCreateDTO, SubFactionUpdateDTO, SubFactionCreateDTO, SubFactionMemberDTO
from typing import List

class SubFactionService:
    def __init__(self, database):
        self.database = database
        self.sub_faction_rank_service = SubFactionRankService(database)
        self.sub_faction_unit_service = SubFactionMemberService(database)
        self.sub_faction_relation_service = SubFactionRelationService(database)
        self.file_service = FileService()

    async def get_all(self, include_ranks: bool, include_units: bool,  include_vassal_subjects:bool, include_overlord:bool, only_overlords:bool) -> List[SubFactionDTO]:
        return await self.database.subfaction.find_many(
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

    async def get_by_id(self, id: str, include_ranks: bool, include_units: bool,  include_vassal_subjects:bool, include_overlord:bool) -> SubFactionDTO:
        return await self.database.subfaction.find_unique( 
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
    
    async def add_rank(self, rank: SubFactionRankCreateDTO) -> SubFactionDTO:
        sub_faction = await self.get_by_id(rank.faction_id, True, True)
        if(not sub_faction): return None

        # Assign Ranks
        await self.sub_faction_rank_service.create(rank)

        return await self.get_by_id(sub_faction.id, True, True)
    
    async def delete_rank(self, id, rank_id: str) -> SubFactionDTO:
        sub_faction = await self.get_by_id(id, True, True)
        if(not sub_faction): return None

        # Remove Ranks
        await self.sub_faction_rank_service.delete(rank_id)

        return await self.get_by_id(sub_faction.id, True, True)
    
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

    async def add_relation(self, relation: SubFactionRankCreateDTO) -> SubFactionDTO:
        sub_faction = await self.get_by_id(relation.faction_id, True, True)
        if(not sub_faction): return None

        sub_faction2 = await self.get_by_id(relation.faction2_id, True, True)
        if(not sub_faction2): return None

        # Assign Relations
        await self.sub_faction_relation_service.create(relation)

        return await self.get_by_id(sub_faction.id, True, True)
    
    async def delete_relation(self, faction_id, faction2_id: str) -> SubFactionDTO:
        sub_faction = await self.get_by_id(id, True, True)
        if(not sub_faction): return None

        sub_faction2 = await self.get_by_id(id, True, True)
        if(not sub_faction2): return None

        # Remove Relations
        await self.sub_faction_relation_service.delete_by_ids(faction_id, faction2_id)

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