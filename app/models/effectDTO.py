from pydantic import BaseModel
from typing import Optional

class EffectBaseDTO(BaseModel):
    name: str
    description: str
    magic_effectiveness: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    essence_recovery: Optional[str]
    vitality: Optional[str]
    range: Optional[str]
    damage: Optional[str]
    armor: Optional[str]
    magic_armor: Optional[str]
    essence: Optional[str]
    agility: Optional[str]
    hit_chance: Optional[str]
    evasion: Optional[str]
    hit_rate: Optional[str]
    movement: Optional[str]
    ammo: Optional[str]
    shield: Optional[str]
    barrier: float
    max_stack: int

class EffectCreateDTO(EffectBaseDTO):
    pass

class EffectUpdateDTO(EffectBaseDTO):
    name: Optional[str]
    description: Optional[str]
    magic_effectiveness: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    essence_recovery: Optional[str]
    vitality: Optional[str]
    range: Optional[str]
    damage: Optional[str]
    armor: Optional[str]
    magic_armor: Optional[str]
    essence: Optional[str]
    agility: Optional[str]
    hit_chance: Optional[str]
    evasion: Optional[str]
    hit_rate: Optional[str]
    movement: Optional[str]
    ammo: Optional[str]
    shield: Optional[str]
    barrier: Optional[float]
    max_stack: Optional[int]

class EffectDTO(EffectBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True