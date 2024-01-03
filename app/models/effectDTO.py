from pydantic import BaseModel
from typing import Optional

class EffectBaseDTO(BaseModel):
    name: str
    description: str
    conditions: Optional[str] = None
    magic_effectiveness: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    armor_piercing: Optional[str]
    spell_piercing: Optional[str]
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
    barrier: Optional[str]
    instant_vitality_recovery: Optional[str]
    instant_essence_recovery: Optional[str]
    instant_physical_damage: Optional[str]
    instant_magical_damage: Optional[str]
    instant_target: Optional[str]
    instant_area_of_effect: Optional[str]
    instant_conditions: Optional[str]
    max_stack: Optional[int]

class EffectCreateDTO(EffectBaseDTO):
    pass

class EffectUpdateDTO(EffectBaseDTO):
    name: Optional[str] = None
    description: Optional[str]
    conditions: Optional[str] = None
    magic_effectiveness: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    armor_piercing: Optional[str]
    spell_piercing: Optional[str]
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
    barrier: Optional[str]
    instant_vitality_recovery: Optional[str]
    instant_essence_recovery: Optional[str]
    instant_physical_damage: Optional[str]
    instant_magical_damage: Optional[str]
    instant_target: Optional[str]
    instant_area_of_effect: Optional[str]
    instant_conditions: Optional[str]
    max_stack: Optional[int]

class EffectDTO(EffectBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True