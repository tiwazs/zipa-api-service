from pydantic import BaseModel
from typing import Optional

class UnitSkillBaseDTO(BaseModel):
    unit_id: str
    skill_id: str

class UnitSkillCreateDTO(UnitSkillBaseDTO):
    pass

class UnitSkillUpdateDTO(UnitSkillBaseDTO):
    unit_id: Optional[str]
    skill_id: Optional[str]

class UnitSkillDTO(UnitSkillBaseDTO):
    id: str
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True