from pydantic import BaseModel
from typing import List, Optional

class DamageCalculationDTO(BaseModel):
    damage: float
    hit_chance: float
    armor: float
    evasion: float
    damage_modifiers: Optional[List[str]] = None

class HealingCalculationDTO(BaseModel):
    healing: float
    hit_chance: float
    healing_modifiers: Optional[List[str]] = None