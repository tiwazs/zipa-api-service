from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.cultureDTO import CultureCreateDTO, CultureUpdateDTO
from ..services.cultureService import CultureService

router = APIRouter(prefix="/cultures", tags=["Cultures"])

msg_not_found = 'Culture not found'

@router.get("/")
async def get_cultures(request: Request, response: Response, by_race_id: str = None, by_race_group_id: str = None,  include_traits: bool = True, include_units: bool = False):
    return await CultureService(request.app.state.db).get_all(by_race_id, by_race_group_id, include_traits, include_units)

@router.get("/{id}")
async def get_culture_by_id(id: str, request: Request, response: Response,  include_traits: bool = True, include_units: bool = False):
    try:
        culture = await CultureService(request.app.state.db).get_by_id(id, include_traits, include_units)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_culture(culture: CultureCreateDTO, request: Request, response: Response):
    try:
        return await CultureService(request.app.state.db).create(culture)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_culture(id: str, culture: CultureUpdateDTO, request: Request, response: Response):
    try:
        culture = await CultureService(request.app.state.db).update(id, culture)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_trait/{id}")
async def add_trait_to_culture(id: str, trait_id: str, request: Request, response: Response):
    try:
        culture = await CultureService(request.app.state.db).add_trait(id, trait_id)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_trait/{id}")
async def remove_trait_from_culture(id: str, trait_id: str, request: Request, response: Response):
    try:
        culture = await CultureService(request.app.state.db).remove_trait(id, trait_id)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@router.put("/add_unit/{id}")
async def add_unit_to_culture(id: str, unit_id: str, request: Request, response: Response):
    try:
        culture = await CultureService(request.app.state.db).add_unit(id, unit_id)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/remove_unit/{id}")
async def remove_unit_from_culture(id: str, unit_id: str, request: Request, response: Response):
    try:
        culture = await CultureService(request.app.state.db).remove_unit(id, unit_id)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_culture(id: str, request: Request, response: Response):
    try:
        culture = await CultureService(request.app.state.db).delete(id)
        if culture is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return culture
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await CultureService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)} 