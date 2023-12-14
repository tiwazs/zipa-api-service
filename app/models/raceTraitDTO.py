from pydantic import BaseModel
from typing import Optional

class RaceTraitBaseDTO(BaseModel):
    unit_id: str
    trait_id: str
    conditions: Optional[str]

class RaceTraitCreateDTO(RaceTraitBaseDTO):
    pass

class RaceTraitUpdateDTO(RaceTraitBaseDTO):
    unit_id: Optional[str]
    trait_id: Optional[str]
    conditions: Optional[str]

class RaceTraitDTO(RaceTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True