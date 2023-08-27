from pydantic import BaseModel
from typing import Optional

class TraitEffectBaseDTO(BaseModel):
    trait_id: str
    effect_id: str
    conditions: Optional[str]
    duration: Optional[str]
    cooldown: Optional[str]

class TraitEffectCreateDTO(TraitEffectBaseDTO):
    pass

class TraitEffectDTO(TraitEffectBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True