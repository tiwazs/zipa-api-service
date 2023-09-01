from pydantic import BaseModel
from typing import List, Optional

class SubFactionBaseDTO(BaseModel):
    name: str
    description: Optional[str] = None
    holdings: Optional[str] = None

# Members
class SubFactionMemberDTO(SubFactionBaseDTO):
    faction_id: str
    unit_id: str
    faction_rank_id: str

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