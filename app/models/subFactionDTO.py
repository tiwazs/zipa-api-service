from pydantic import BaseModel
from typing import List, Optional

# Members
class SubFactionMemberDTO(BaseModel):
    faction_id: str
    unit_id: str
    faction_rank_id: str

# Ranks
class SubFactionRankDTO(BaseModel):
    faction_id: str
    name: str
    description: Optional[str] = None
    rank: int

class SubFactionRankCreateDTO(SubFactionRankDTO):
    pass

class SubFactionRankUpdateDTO(SubFactionRankDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    rank: Optional[int] = None


# SubFactions
class SubFactionBaseDTO(BaseModel):
    name: str
    description: Optional[str] = None
    holdings: Optional[str] = None

class SubFactionCreateDTO(SubFactionBaseDTO):
    user_id: str

class SubFactionUpdateDTO(SubFactionBaseDTO):
    name: Optional[str]
    description: Optional[str] = None
    holdings: Optional[str] = None

class SubFactionDTO(SubFactionBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True