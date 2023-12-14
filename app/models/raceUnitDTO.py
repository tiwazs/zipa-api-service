from pydantic import BaseModel
from typing import List, Optional

class RaceUnitDTO(BaseModel):
    faction_id: str
    unit_specialization_id: str

class RaceUnitCreateDTO(RaceUnitDTO):
    pass

class RaceUnitUpdateDTO(RaceUnitDTO):
    pass

class RaceUnitDTO(RaceUnitDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True