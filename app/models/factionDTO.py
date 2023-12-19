from pydantic import BaseModel
from typing import List, Optional

# Members
class FactionMemberDTO(BaseModel):
    faction_id: str
    unit_id: str
    faction_rank_id: str

# Ranks
class FactionRankDTO(BaseModel):
    faction_id: str
    name: str
    description: Optional[str] = None
    rank: int

class FactionRankCreateDTO(FactionRankDTO):
    pass

class FactionRankUpdateDTO(FactionRankDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    rank: Optional[int] = None


# Factions
class FactionBaseDTO(BaseModel):
    name: str
    description: Optional[str] = None
    holdings: Optional[str] = None

class FactionCreateDTO(FactionBaseDTO):
    user_id: str

class FactionUpdateDTO(FactionBaseDTO):
    name: Optional[str]
    description: Optional[str] = None
    holdings: Optional[str] = None

class FactionDTO(FactionBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Faction Relations
class FactionRelationDTO(BaseModel):
    faction_id: str
    faction2_id: str
    type: str