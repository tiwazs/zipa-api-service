from fastapi import APIRouter, Request, Response, status

from ..models.skillDTO import SkillDTO, SkillUpdateDTO, SkillCreateDTO
from ..services.skillService import SkillService

router = APIRouter(prefix="/skills", tags=["Skills"])

msg_not_found = 'Skill not found'

@router.get("/")
async def get_skills(request: Request, response: Response, include_type: bool = True, include_effects: bool = True):
    return await SkillService(request.app.state.db).get_all(include_type, include_effects)

@router.get("/{id}")
async def get_skill_by_id(id: str, request: Request, response: Response, include_type: bool = True, include_effects: bool = True):
    try:
        skill = await SkillService(request.app.state.db).get_by_id(id, include_type, include_effects)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_skill(skill: SkillCreateDTO, request: Request, response: Response):
        return await SkillService(request.app.state.db).create(skill)

    
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

@router.put("/add_type/{id}")
async def add_type_to_skill(id: str, skill_type_id: str, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).add_type(id, skill_type_id)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_type/{id}")
async def remove_type_from_skill(id: str, skill_type_id: str, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).remove_type(id, skill_type_id)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_effect/{id}")
async def add_effect_to_skill(id: str, effect_id: str, duration: int, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).add_effect(id, effect_id, duration)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_effect/{id}")
async def remove_effect_from_skill(id: str, effect_id: str, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).remove_effect(id, effect_id)
        if skill is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return skill
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/update_effect/{id}")
async def update_effect_from_skill(id: str, effect_id: str, duration: int, request: Request, response: Response):
    try:
        skill = await SkillService(request.app.state.db).update_effect(id, effect_id, duration)
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