from pydantic import BaseModel
from typing import List, Optional

# Available Specializations
class AvailableSpecializationDTO(BaseModel):
    faction_id: str
    unit_id: str
    faction_rank_id: str

# Trait
class BeliefTraitBaseDTO(BaseModel):
    unit_id: str
    trait_id: str
    conditions: Optional[str]

class BeliefTraitCreateDTO(BeliefTraitBaseDTO):
    pass

class BeliefTraitUpdateDTO(BeliefTraitBaseDTO):
    unit_id: Optional[str]
    trait_id: Optional[str]
    conditions: Optional[str]

class BeliefTraitDTO(BeliefTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Unit Specialization
class BeliefUnitBaseDTO(BaseModel):
    belief_id: str
    unit_specialization_id: str

class BeliefUnitCreateDTO(BeliefUnitBaseDTO):
    pass

class BeliefUnitUpdateDTO(BeliefUnitBaseDTO):
    belief_id: Optional[str]
    unit_specialization_id: Optional[str]

class BeliefUnitDTO(BeliefUnitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Belief
class BeliefBaseDTO(BaseModel):
    name: str
    description: str
    identity: Optional[str] = None
    aspects: Optional[str] = None

class BeliefCreateDTO(BeliefBaseDTO):
    unit_specialization_ids: Optional[List[str]] = None

class BeliefUpdateDTO(BeliefBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    identity: Optional[str] = None
    aspects: Optional[str] = None

class BeliefDTO(BeliefBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True