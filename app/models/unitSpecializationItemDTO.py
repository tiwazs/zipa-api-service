from pydantic import BaseModel
from typing import Optional

class UnitSpecializationItemBaseDTO(BaseModel):
    unit_id: str
    item_id: str
    quantity: float

class UnitSpecializationItemCreateDTO(UnitSpecializationItemBaseDTO):
    pass

class UnitSpecializationItemUpdateDTO(UnitSpecializationItemBaseDTO):
    unit_id: Optional[str]
    item_id: Optional[str]
    quantity: Optional[float]

class UnitSpecializationItemDTO(UnitSpecializationItemBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True