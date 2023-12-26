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
    ascended: Optional[bool] = False
    ascended_params: Optional[str] = None
    race_id: str
    culture_id: str
    belief_id: str
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
    ascended: Optional[bool]
    ascended_params: Optional[str]
    race_id: Optional[str]
    culture_id: Optional[str]
    belief_id: Optional[str]
    specialization_id: Optional[str]
    skill_picks: Optional[str] = None
    rank: Optional[int] = None

class UnitDTO(UnitBaseDTO):
    id: str
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        orm_mode = True