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
    cooldown: Optional[str]
    channeled: Optional[str]
    projectile: Optional[bool]
    target: Optional[str]
    skill_on: Optional[str]

class SkillEffectToCreate(BaseModel):
    effect_id: str
    duration: str

class SkillCreateDTO(SkillBaseDTO):
    skill_type_ids: Optional[List[str]] = None
    skill_effect_ids: Optional[List[SkillEffectToCreate]] = None


class SkillUpdateDTO(SkillBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    conditions: Optional[str] = None
    physical_damage: Optional[str] = None
    magical_damage: Optional[str] = None
    healing: Optional[str] = None
    essence_recovery: Optional[str] = None
    range: Optional[str] = None
    area_of_effect: Optional[str] = None
    essence_cost: Optional[str] = None
    vitality_cost: Optional[str] = None
    cooldown: Optional[str] = None
    channeled: Optional[str] = None
    projectile: Optional[bool] = None
    target: Optional[str] = None
    skill_on: Optional[str] = None

class SkillDTO(SkillBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True