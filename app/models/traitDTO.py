from pydantic import BaseModel
from typing import Optional, List

class TraitBaseDTO(BaseModel):
    name: str
    description: str

class TraitCreateDTO(TraitBaseDTO):
    effect_ids: Optional[List[str]] = None

class TraitUpdateDTO(TraitBaseDTO):
    name: Optional[str]
    description: Optional[str]

class TraitDTO(TraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True