from pydantic import BaseModel
from typing import Optional

class UnitTraitBaseDTO(BaseModel):
    unit_id: str
    trait_id: str

class UnitTraitCreateDTO(UnitTraitBaseDTO):
    pass

class UnitTraitUpdateDTO(UnitTraitBaseDTO):
    unit_id: Optional[str]
    trait_id: Optional[str]

class UnitTraitDTO(UnitTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True