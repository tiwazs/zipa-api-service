from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.raceDTO import RaceCreateDTO, RaceUpdateDTO
from ..services.raceService import RaceService

router = APIRouter(prefix="/races", tags=["Races"])

msg_not_found = 'Race not found'

@router.get("/")
async def get_races(request: Request, response: Response,  include_traits: bool = True, include_cultures: bool = False, include_beliefs: bool = False, include_units: bool = False):
    return await RaceService(request.app.state.db).get_all(include_traits, include_cultures, include_beliefs, include_units)

@router.get("/{id}")
async def get_race_by_id(id: str, request: Request, response: Response,  include_traits: bool = True, include_cultures: bool = False, include_beliefs: bool = False, include_units: bool = False):
    try:
        race = await RaceService(request.app.state.db).get_by_id(id, include_traits, include_cultures, include_beliefs, include_units)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_race(race: RaceCreateDTO, request: Request, response: Response):
    try:
        return await RaceService(request.app.state.db).create(race)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_race(id: str, race: RaceUpdateDTO, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).update(id, race)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_trait/{id}")
async def add_trait_to_race(id: str, trait_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).add_trait(id, trait_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_trait/{id}")
async def remove_trait_from_race(id: str, trait_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).remove_trait(id, trait_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_culture/{id}")
async def add_culture_to_race(id: str, culture_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).add_culture(id, culture_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_culture/{id}")
async def remove_culture_from_race(id: str, culture_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).remove_culture(id, culture_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_belief/{id}")
async def add_belief_to_race(id: str, trait_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).add_belief(id, trait_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_belief/{id}")
async def remove_belief_from_race(id: str, belief_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).remove_belief(id, belief_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
'''
@router.put("/add_unit/{id}")
async def add_unit_to_race(id: str, unit_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).add_unit(id, unit_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/remove_unit/{id}")
async def remove_unit_from_race(id: str, unit_id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).remove_unit(id, unit_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
'''

@router.delete("/{id}")
async def delete_race(id: str, request: Request, response: Response):
    try:
        race = await RaceService(request.app.state.db).delete(id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await RaceService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)} 