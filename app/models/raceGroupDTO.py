from pydantic import BaseModel
from typing import List, Optional

# RaceGroup
class RaceGroupBaseDTO(BaseModel):
    name: str
    description: str

class RaceGroupCreateDTO(RaceGroupBaseDTO):
    pass

class RaceGroupUpdateDTO(RaceGroupBaseDTO):
    name: Optional[str] = None
    description: Optional[str] = None

class RaceGroupDTO(RaceGroupBaseDTO):
    id: int
    created_at: str
    updated_at: str
    class Config:
        orm_mode = True