from fastapi import APIRouter, File, Request, Response, UploadFile, status

from ..models.effectDTO import EffectDTO, EffectUpdateDTO, EffectCreateDTO
from ..services.effectService import EffectService

router = APIRouter(prefix="/effects", tags=["Effects"])

msg_not_found = 'Effect not found'

@router.get("/")
async def get_effects(request: Request, response: Response):
    return await EffectService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_effect_by_id(id: str, request: Request, response: Response):
    try:
        effect = await EffectService(request.app.state.db).get_by_id(id)
        if effect is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return effect
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_effect(effect: EffectCreateDTO, request: Request, response: Response):
    try:
        return await EffectService(request.app.state.db).create(effect)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_effect(id: str, effect: EffectUpdateDTO, request: Request, response: Response):
    try:
        effect = await EffectService(request.app.state.db).update(id, effect)
        if effect is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return effect
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.delete("/{id}")
async def delete_effect(id: str, request: Request, response: Response):
    try:
        effect = await EffectService(request.app.state.db).delete(id)
        if effect is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return effect
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await EffectService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}