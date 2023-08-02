from pydantic import BaseModel
from typing import List, Optional

class SkillBaseDTO(BaseModel):
    name: str
    description: str
    conditions: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    vitality_recovery: Optional[str]
    essence_recovery: Optional[str]
    range: Optional[str]
    area_of_effect: Optional[str]
    essence_cost: Optional[str]
    vitality_cost: Optional[str]
    cooldown: Optional[float]
    channeled: Optional[bool]
    target: Optional[str]
    skill_on: Optional[str]

class SkillEffectToCreate(BaseModel):
    effect_id: str
    duration: float

class SkillCreateDTO(SkillBaseDTO):
    skill_type_ids: Optional[List[str]] = None
    skill_effect_ids: Optional[List[SkillEffectToCreate]] = None


class SkillUpdateDTO(SkillBaseDTO):
    name: Optional[str]
    description: Optional[str]
    conditions: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    essence_recovery: Optional[str]
    range: Optional[str]
    area_of_effect: Optional[str]
    essence_cost: Optional[str]
    vitality_cost: Optional[str]
    cooldown: Optional[float]
    channeled: Optional[bool]
    target: Optional[str]
    skill_on: Optional[str]

class SkillDTO(SkillBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True