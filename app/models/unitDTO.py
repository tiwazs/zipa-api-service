from pydantic import BaseModel
from typing import List, Optional

class UnitBaseDTO(BaseModel):
    name: str
    title: Optional[str] = None
    prefix_title: Optional[str] = None
    description: Optional[str] = None
    base_vitality: float
    base_strength: float
    base_dexterity: float
    base_mind: float
    base_faith: float
    base_essence: float
    base_agility: float
    base_hit_chance: float
    base_evasion: float
    faction_id: str
    specialization_id: str
    skill_picks: Optional[str] = None
    rank: Optional[int] = None

class UnitItemCreateDTO(BaseModel):
    item_id: str
    quantity: int

class UnitCreateDTO(UnitBaseDTO):
    user_id: str
    items: Optional[List[UnitItemCreateDTO]] = None

class UnitUpdateDTO(UnitBaseDTO):
    name: Optional[str]
    title: Optional[str] = None
    prefix_title: Optional[str] = None
    description: Optional[str]
    base_vitality: Optional[float]
    base_strength: Optional[float]
    base_dexterity: Optional[float]
    base_mind: Optional[float]
    base_faith: Optional[float]
    base_essence: Optional[float]
    base_agility: Optional[float]
    base_hit_chance: Optional[float]
    base_evasion: Optional[float]
    faction_id: Optional[str]
    specialization_id: Optional[str]
    skill_picks: Optional[str] = None
    rank: Optional[int] = None

class UnitDTO(UnitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True