from pydantic import BaseModel
from typing import List, Optional

class UnitBaseDTO(BaseModel):
    name: str
    description: str
    vitality: float
    range: float
    damage: float
    armor: float
    magic_armor: float
    essence: float
    agility: float
    hit_chance: float
    evasion: float
    hit_rate: float
    movement: float
    ammo: float
    shield: float
    tier: int

class UnitItemCreateDTO(BaseModel):
    item_id: str
    quantity: int

class UnitCreateDTO(UnitBaseDTO):
    trait_ids: Optional[List[str]] = None
    skill_ids: Optional[List[str]] = None
    items: Optional[List[UnitItemCreateDTO]] = None

class UnitUpdateDTO(UnitBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    vitality: Optional[float] = None
    range: Optional[float] = None
    damage: Optional[float] = None
    armor: Optional[float] = None
    magic_armor: Optional[float] = None
    essence: Optional[float] = None
    agility: Optional[float] = None
    hit_chance: Optional[float] = None
    evasion: Optional[float] = None
    hit_rate: Optional[float] = None
    movement: Optional[float] = None
    ammo: Optional[float] = None
    shield: Optional[float] = None
    tier: Optional[int] = None

class UnitDTO(UnitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True