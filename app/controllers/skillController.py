from fastapi import APIRouter, Request, Response, status

from ..models.skillDTO import SkillDTO, SkillUpdateDTO, SkillCreateDTO
from ..services.skillService import SkillService

router = APIRouter(prefix="/skills", tags=["Skills"])

msg_not_found = 'Skill not found'

@router.get("/")
async def get_skills(request: Request, response: Response):
    return await SkillService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_skill_by_id(id: str, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).get_by_id(id)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_skill(skill: SkillCreateDTO, request: Request, response: Response):
    try:
        return await SkillService(request.app.state.db).create(skill)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_skill(id: str, skill: SkillUpdateDTO, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).update(id, skill)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.delete("/{id}")
async def delete_skill(id: str, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).delete(id)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}