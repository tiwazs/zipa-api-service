from pydantic import BaseModel
from typing import Optional

class TraitBaseDTO(BaseModel):
    name: str
    description: str
    cooldown: float

class TraitCreateDTO(TraitBaseDTO):
    pass

class TraitUpdateDTO(TraitBaseDTO):
    name: Optional[str]
    description: Optional[str]
    cooldown: Optional[float]

class TraitDTO(TraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True