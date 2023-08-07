from pydantic import BaseModel
from typing import Optional

class UnitSpecializationSkillBaseDTO(BaseModel):
    unit_id: str
    skill_id: str

class UnitSpecializationSkillCreateDTO(UnitSpecializationSkillBaseDTO):
    pass

class UnitSpecializationSkillUpdateDTO(UnitSpecializationSkillBaseDTO):
    unit_id: Optional[str]
    skill_id: Optional[str]

class UnitSpecializationSkillDTO(UnitSpecializationSkillBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True