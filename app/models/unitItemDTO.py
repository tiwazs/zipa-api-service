from pydantic import BaseModel
from typing import Optional

class UnitItemBaseDTO(BaseModel):
    unit_id: str
    item_id: str
    quantity: float

class UnitItemCreateDTO(UnitItemBaseDTO):
    pass

class UnitItemUpdateDTO(UnitItemBaseDTO):
    unit_id: Optional[str]
    item_id: Optional[str]
    quantity: Optional[float]

class UnitItemDTO(UnitItemBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True