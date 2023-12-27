from pydantic import BaseModel
from typing import List, Optional

class ItemBaseDTO(BaseModel):
    name: str
    description: str
    conditions: Optional[str]
    rarity: Optional[str]
    is_weapon: Optional[bool]
    object_type: Optional[str]
    magic_effectiveness: Optional[str]
    physical_damage: Optional[str]
    magical_damage: Optional[str]
    healing: Optional[str]
    armor_piercing: Optional[str]
    spell_piercing: Optional[str]
    vitality_recovery: Optional[str]
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
    dexterity_requirement: Optional[float]
    strength_requirement: Optional[float]
    mind_requirement: Optional[float]
    faith_requirement: Optional[float]
    weight: Optional[float]

class ItemSkillToCreate(BaseModel):
    skill_id: str
    essence_cost: float
    cooldown: float
class ItemCreateDTO(ItemBaseDTO):
    skills: Optional[List[ItemSkillToCreate]] = None

class ItemUpdateDTO(ItemBaseDTO):
    name: Optional[str]  = None
    description: Optional[str]  = None
    conditions: Optional[str]  = None
    rarity: Optional[str]  = None
    is_weapon: Optional[bool] = None
    object_type: Optional[str]  = None
    magic_effectiveness: Optional[str]  = None
    physical_damage: Optional[str]  = None
    magical_damage: Optional[str]  = None
    healing: Optional[str]  = None
    armor_piercing: Optional[str]  = None
    spell_piercing: Optional[str]  = None
    essence_recovery: Optional[str]  = None
    vitality: Optional[str]  = None
    range: Optional[str]  = None
    damage: Optional[str]  = None
    armor: Optional[str]  = None
    magic_armor: Optional[str]  = None
    essence: Optional[str]  = None
    agility: Optional[str]  = None
    hit_chance: Optional[str]  = None
    evasion: Optional[str]  = None
    hit_rate: Optional[str]  = None
    movement: Optional[str]  = None
    ammo: Optional[str]  = None
    shield: Optional[str]  = None
    dexterity_requirement: Optional[float]  = None
    strength_requirement: Optional[float]  = None
    mind_requirement: Optional[float]  = None
    faith_requirement: Optional[float]  = None
    weight: Optional[float]  = None

class ItemDTO(ItemBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True