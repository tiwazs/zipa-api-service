from pydantic import BaseModel
from typing import List, Optional

# Available Specializations
class AvailableSpecializationDTO(BaseModel):
    faction_id: str
    unit_id: str
    faction_rank_id: str

# Trait
class CultureTraitBaseDTO(BaseModel):
    unit_id: str
    trait_id: str
    conditions: Optional[str]

class CultureTraitCreateDTO(CultureTraitBaseDTO):
    pass

class CultureTraitUpdateDTO(CultureTraitBaseDTO):
    unit_id: Optional[str]
    trait_id: Optional[str]
    conditions: Optional[str]

class CultureTraitDTO(CultureTraitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Unit Specialization
class CultureUnitBaseDTO(BaseModel):
    culture_id: str
    unit_specialization_id: str

class CultureUnitCreateDTO(CultureUnitBaseDTO):
    pass

class CultureUnitUpdateDTO(CultureUnitBaseDTO):
    culture_id: Optional[str]
    unit_specialization_id: Optional[str]

class CultureUnitDTO(CultureUnitBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True

# Culture
class CultureBaseDTO(BaseModel):
    name: str
    description: str
    identity: Optional[str] = None
    aspects: Optional[str] = None

class CultureCreateDTO(CultureBaseDTO):
    unit_specialization_ids: Optional[List[str]] = None

class CultureUpdateDTO(CultureBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None
    identity: Optional[str] = None
    aspects: Optional[str] = None

class CultureDTO(CultureBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True