from pydantic import BaseModel
from typing import Optional, List

class TraitBaseDTO(BaseModel):
    name: str
    description: str
    conditions: Optional[str]
    cooldown: Optional[float]

class TraitCreateDTO(TraitBaseDTO):
    effect_ids: Optional[List[str]] = None

class TraitUpdateDTO(TraitBaseDTO):
    name: Optional[str]
    description: Optional[str]
    conditions: Optional[str]
    cooldown: Optional[float]


class TraitDTO(TraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True