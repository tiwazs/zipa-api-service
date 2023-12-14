from pydantic import BaseModel
from typing import List, Optional

class RaceBaseDTO(BaseModel):
    name: str
    description: str
    identity: Optional[str] = None
    aspects: Optional[str] = None

class RaceCreateDTO(RaceBaseDTO):
    unit_specialization_ids: Optional[List[str]] = None

class RaceUpdateDTO(RaceBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    identity: Optional[str] = None
    aspects: Optional[str] = None

class RaceDTO(RaceBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True