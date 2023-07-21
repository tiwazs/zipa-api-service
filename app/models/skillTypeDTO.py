from pydantic import BaseModel
from typing import Optional

class SkillTypeBaseDTO(BaseModel):
    name: str
    description: str

class SkillTypeCreateDTO(SkillTypeBaseDTO):
    pass

class SkillTypeUpdateDTO(SkillTypeBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None

class SkillTypeDTO(SkillTypeBaseDTO):
    id: str
    class Config:
        orm_mode = True