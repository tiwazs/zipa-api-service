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
    equipped: Optional[bool] = False

class UnitItemUpdateDTO(BaseModel):
    new_item_id: Optional[str] = None
    quantity: Optional[int] = None
    equipped: Optional[bool] = None

class UnitCreateDTO(UnitBaseDTO):
    user_id: str
    items: Optional[List[UnitItemCreateDTO]] = None

class UnitUpdateDTO(UnitBaseDTO):
    name: Optional[str] = None
    title: Optional[str] = None
    prefix_title: Optional[str] = None
    description: Optional[str] = None
    base_vitality: Optional[float] = None
    base_strength: Optional[float] = None
    base_dexterity: Optional[float] = None
    base_mind: Optional[float] = None
    base_faith: Optional[float] = None
    base_essence: Optional[float] = None
    base_agility: Optional[float] = None
    base_hit_chance: Optional[float] = None
    base_evasion: Optional[float] = None
    ascended: Optional[bool] = None
    ascended_params: Optional[str] = None
    race_id: Optional[str] = None
    culture_id: Optional[str] = None
    belief_id: Optional[str] = None
    specialization_id: Optional[str] = None
    skill_picks: Optional[str] = None
    rank: Optional[int] = None

class UnitDTO(UnitBaseDTO):
    id: str
    created_at: Optional[str]
    updated_at: Optional[str]
    class Config:
        orm_mode = True