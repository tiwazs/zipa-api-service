from pydantic import BaseModel
from typing import Optional

class SkillBaseDTO(BaseModel):
    name: str
    description: str
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    essence_recovery: Optional[str]
    range: Optional[str]
    area_of_effect: Optional[str]
    essence_cost: Optional[str]
    vitality_cost: Optional[str]
    cooldown: float
    channeled: bool
    target: Optional[str]
    skill_on: Optional[str]

class SkillCreateDTO(SkillBaseDTO):
    pass

class SkillUpdateDTO(SkillBaseDTO):
    name: Optional[str]
    description: Optional[str]
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