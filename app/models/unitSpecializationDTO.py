from pydantic import BaseModel
from typing import List, Optional

class UnitSpecializationBaseDTO(BaseModel):
    name: str
    description: str
    vitality: float
    strength: float
    dexterity: float
    mind: float
    faith: float
    armor: float
    magic_armor: float
    essence: float
    agility: float
    hit_chance: float
    evasion: float
    hit_rate: float
    movement: float
    weapon_proficiencies: str
    tier: int

class UnitSpecializationItemCreateDTO(BaseModel):
    item_id: str
    quantity: int

class UnitSpecializationCreateDTO(UnitSpecializationBaseDTO):
    trait_ids: Optional[List[str]] = None
    skill_ids: Optional[List[str]] = None
    items: Optional[List[UnitSpecializationItemCreateDTO]] = None

class UnitSpecializationUpdateDTO(UnitSpecializationBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    vitality: Optional[float] = None
    damage: Optional[float] = None
    armor: Optional[float] = None
    magic_armor: Optional[float] = None
    essence: Optional[float] = None
    agility: Optional[float] = None
    hit_chance: Optional[float] = None
    evasion: Optional[float] = None
    hit_rate: Optional[float] = None
    movement: Optional[float] = None
    weapon_proficiencies: Optional[str] = None
    tier: Optional[int] = None

class UnitSpecializationDTO(UnitSpecializationBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True