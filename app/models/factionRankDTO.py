from pydantic import BaseModel
from typing import List, Optional

class FactionRankBaseDTO(BaseModel):
    faction_id: str
    name: str
    description: Optional[str] = None
    rank: int

class FactionRankCreateDTO(FactionRankBaseDTO):
    pass

class FactionRankUpdateDTO(FactionRankBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    rank: Optional[int] = None

class FactionRankDTO(FactionRankBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True