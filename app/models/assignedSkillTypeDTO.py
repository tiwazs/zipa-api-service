from pydantic import BaseModel
from typing import Optional

class AssignedSkillTypeBaseDTO(BaseModel):
    skill_id: str
    skill_type_id: str

class AssignedSkillTypeCreateDTO(AssignedSkillTypeBaseDTO):
    pass

class AssignedSkillTypeDTO(AssignedSkillTypeBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True