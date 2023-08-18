from pydantic import BaseModel
from typing import Optional

class FactionTraitBaseDTO(BaseModel):
    unit_id: str
    trait_id: str
    conditions: Optional[str]

class FactionTraitCreateDTO(FactionTraitBaseDTO):
    pass

class FactionTraitUpdateDTO(FactionTraitBaseDTO):
    unit_id: Optional[str]
    trait_id: Optional[str]
    conditions: Optional[str]

class FactionTraitDTO(FactionTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True