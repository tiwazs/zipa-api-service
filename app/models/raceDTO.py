from pydantic import BaseModel
from typing import List, Optional

# Available Cultures
class RaceCultureBaseDTO(BaseModel):
    race_id: str
    culture_id: str

class RaceCultureCreateDTO(RaceCultureBaseDTO):
    pass

class RaceCultureUpdateDTO(RaceCultureBaseDTO):
    race_id: Optional[str]
    culture_id: Optional[str]

class RaceCultureDTO(RaceCultureBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Available Beliefs
class RaceBeliefBaseDTO(BaseModel):
    race_id: str
    belief_id: str

class RaceBeliefCreateDTO(RaceBeliefBaseDTO):
    pass

class RaceBeliefUpdateDTO(RaceBeliefBaseDTO):
    race_id: Optional[str]
    belief_id: Optional[str]

class RaceBeliefDTO(RaceBeliefBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Race
class RaceBaseDTO(BaseModel):
    name: str
    description: str
    identity: Optional[str] = None
    aspects: Optional[str] = None

class RaceCreateDTO(RaceBaseDTO):
    unit_specialization_ids: Optional[List[str]] = None

class RaceUpdateDTO(RaceBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    identity: Optional[str] = None
    aspects: Optional[str] = None

class RaceDTO(RaceBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True