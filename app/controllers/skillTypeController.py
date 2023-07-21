from fastapi import APIRouter, Request, Response, status

from ..models.skillTypeDTO import SkillTypeDTO, SkillTypeUpdateDTO, SkillTypeCreateDTO
from ..services.skillTypeService import SkillTypeService

router = APIRouter(prefix="/skillTypes", tags=["SkillTypes"])

msg_not_found = 'SkillType not found'

@router.get("/")
async def get_skillTypes(request: Request, response: Response):
    return await SkillTypeService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_skillType_by_id(id: str, request: Request, response: Response):
    try:
        skill_type = await SkillTypeService(request.app.state.db).get_by_id(id)
        if skill_type is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill_type
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_skillType(skill_type: SkillTypeCreateDTO, request: Request, response: Response):
    try:
        return await SkillTypeService(request.app.state.db).create(skill_type)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/{id}")
async def update_skillType(id: str, skill_type: SkillTypeUpdateDTO, request: Request, response: Response):
    try:
        skill_type = await SkillTypeService(request.app.state.db).update(id, skill_type)
        if skill_type is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill_type
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_skillType(id: str, request: Request, response: Response):
    try:
        skill_type = await SkillTypeService(request.app.state.db).delete(id)
        if skill_type is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill_type
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}