from pydantic import BaseModel
from typing import Optional

class UnitBaseDTO(BaseModel):
    unit_id: str
    item_id: str
    quantity: float

class UnitCreateDTO(UnitBaseDTO):
    pass

class UnitUpdateDTO(UnitBaseDTO):
    unit_id: Optional[str]
    item_id: Optional[str]
    quantity: Optional[float]

class UnitDTO(UnitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True