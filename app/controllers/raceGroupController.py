from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.raceGroupDTO import RaceGroupCreateDTO, RaceGroupUpdateDTO
from ..services.raceGroupService import RaceGroupService

router = APIRouter(prefix="/race_groups", tags=["RaceGroups"])

msg_not_found = 'RaceGroup not found'

@router.get("/")
async def get_race_groups(request: Request, response: Response):
    return await RaceGroupService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_race_group_by_id(id: str, request: Request, response: Response):
    try:
        race_group = await RaceGroupService(request.app.state.db).get_by_id(id)
        if race_group is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race_group
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_race_group(race_group: RaceGroupCreateDTO, request: Request, response: Response):
    try:
        return await RaceGroupService(request.app.state.db).create(race_group)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_race_group(id: str, race_group: RaceGroupUpdateDTO, request: Request, response: Response):
    try:
        race_group = await RaceGroupService(request.app.state.db).update(id, race_group)
        if race_group is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race_group
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_race_group(id: str, request: Request, response: Response):
    try:
        race_group = await RaceGroupService(request.app.state.db).delete(id)
        if race_group is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race_group
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await RaceGroupService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)} 