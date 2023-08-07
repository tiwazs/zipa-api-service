from pydantic import BaseModel
from typing import Optional

class UnitSpecializationTraitBaseDTO(BaseModel):
    unit_id: str
    trait_id: str

class UnitSpecializationTraitCreateDTO(UnitSpecializationTraitBaseDTO):
    pass

class UnitSpecializationTraitUpdateDTO(UnitSpecializationTraitBaseDTO):
    unit_id: Optional[str]
    trait_id: Optional[str]

class UnitSpecializationTraitDTO(UnitSpecializationTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True