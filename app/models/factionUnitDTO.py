from pydantic import BaseModel
from typing import List, Optional

class FactionUnitDTO(BaseModel):
    faction_id: str
    unit_id: str

class FactionUnitCreateDTO(FactionUnitDTO):
    pass

class FactionUnitUpdateDTO(FactionUnitDTO):
    pass

class FactionUnitDTO(FactionUnitDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True