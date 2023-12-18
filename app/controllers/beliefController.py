from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.beliefDTO import BeliefCreateDTO, BeliefUpdateDTO
from ..services.beliefService import BeliefService

router = APIRouter(prefix="/beliefs", tags=["Beliefs"])

msg_not_found = 'Belief not found'

@router.get("/")
async def get_beliefs(request: Request, response: Response,  include_traits: bool = True, include_units: bool = False):
    return await BeliefService(request.app.state.db).get_all(include_traits, include_units)

@router.get("/{id}")
async def get_belief_by_id(id: str, request: Request, response: Response,  include_traits: bool = True, include_units: bool = False):
    try:
        belief = await BeliefService(request.app.state.db).get_by_id(id, include_traits, include_units)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_belief(belief: BeliefCreateDTO, request: Request, response: Response):
    try:
        return await BeliefService(request.app.state.db).create(belief)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_belief(id: str, belief: BeliefUpdateDTO, request: Request, response: Response):
    try:
        belief = await BeliefService(request.app.state.db).update(id, belief)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_trait/{id}")
async def add_trait_to_belief(id: str, trait_id: str, request: Request, response: Response):
    try:
        belief = await BeliefService(request.app.state.db).add_trait(id, trait_id)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_trait/{id}")
async def remove_trait_from_belief(id: str, trait_id: str, request: Request, response: Response):
    try:
        belief = await BeliefService(request.app.state.db).remove_trait(id, trait_id)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@router.put("/add_unit/{id}")
async def add_unit_to_belief(id: str, unit_id: str, request: Request, response: Response):
    try:
        belief = await BeliefService(request.app.state.db).add_unit(id, unit_id)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/remove_unit/{id}")
async def remove_unit_from_belief(id: str, unit_id: str, request: Request, response: Response):
    try:
        belief = await BeliefService(request.app.state.db).remove_unit(id, unit_id)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_belief(id: str, request: Request, response: Response):
    try:
        belief = await BeliefService(request.app.state.db).delete(id)
        if belief is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return belief
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await BeliefService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)} 