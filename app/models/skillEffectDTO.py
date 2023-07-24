from pydantic import BaseModel
from typing import Optional

class SkillEffectBaseDTO(BaseModel):
    skill_id: str
    effect_id: str
    duration: float

class SkillEffectCreateDTO(SkillEffectBaseDTO):
    pass

class SkillEffectUpdateDTO():
    duration: Optional[float] = None

class SkillEffectDTO(SkillEffectBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True