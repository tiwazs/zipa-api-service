from fastapi import APIRouter, Request, Response, status

from ..models.traitDTO import TraitDTO, TraitUpdateDTO, TraitCreateDTO
from ..services.traitService import TraitService

router = APIRouter(prefix="/traits", tags=["Traits"])

msg_not_found = 'Trait not found'

@router.get("/")
async def get_traits(request: Request, response: Response):
    return await TraitService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_trait_by_id(id: str, request: Request, response: Response):
    try:
        trait = await TraitService(request.app.state.db).get_by_id(id)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_trait(trait: TraitCreateDTO, request: Request, response: Response):
    try:
        return await TraitService(request.app.state.db).create(trait)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_trait(id: str, trait: TraitUpdateDTO, request: Request, response: Response):
    try:
        trait = await TraitService(request.app.state.db).update(id, trait)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.delete("/{id}")
async def delete_trait(id: str, request: Request, response: Response):
    try:
        trait = await TraitService(request.app.state.db).delete(id)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}