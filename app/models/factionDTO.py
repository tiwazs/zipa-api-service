from pydantic import BaseModel
from typing import List, Optional

class FactionBaseDTO(BaseModel):
    name: str
    description: str
    identity: Optional[str] = None
    aspects: Optional[str] = None



class FactionCreateDTO(FactionBaseDTO):
    unit_ids: Optional[List[str]] = None

class FactionUpdateDTO(FactionBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    identity: Optional[str] = None
    aspects: Optional[str] = None

class FactionDTO(FactionBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True