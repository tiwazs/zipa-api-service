from pydantic import BaseModel
from typing import List, Optional

class UnitGenerationBaseDTO(BaseModel):
    vitality: float
    strength: float
    dexterity: float
    mind: float
    faith: float
    essence: float
    agility: float
    hit_chance: float
    evasion: float