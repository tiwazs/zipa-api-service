from fastapi import APIRouter, Request, Response, status


from ..models.itemDTO import ItemDTO, ItemUpdateDTO, ItemCreateDTO
from ..models.itemSkillDTO import ItemSkillCreateDTO, ItemSkillUpdateDTO
from ..services.itemService import ItemService

router = APIRouter(prefix="/items", tags=["Items"])

msg_not_found = 'Item not found'

@router.get("/")
async def get_items(request: Request, response: Response, include_skills: bool = True):
    return await ItemService(request.app.state.db).get_all(include_skills)

@router.get("/{id}")
async def get_item_by_id(id: str, request: Request, response: Response, include_skills: bool = True):
    try:
        item = await ItemService(request.app.state.db).get_by_id(id, include_skills)
        if item is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return item
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_item(item: ItemCreateDTO, request: Request, response: Response):
    try:
        return await ItemService(request.app.state.db).create(item)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/update/{id}")
async def update_item(id: str, item: ItemUpdateDTO, request: Request, response: Response):
    try:
        item = await ItemService(request.app.state.db).update(id, item)
        if item is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return item
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_skill")
async def add_skill_to_item(id: str, item_skill: ItemSkillCreateDTO, request: Request, response: Response):
    try:
        item = await ItemService(request.app.state.db).add_skill(item_skill)
        if item is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return item
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_skill/{id}")
async def remove_skill_from_item(id: str, skill_id: str, request: Request, response: Response):
    try:
        item = await ItemService(request.app.state.db).remove_skill(id, skill_id)
        if item is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return item
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/update_skill")
async def update_skill_from_item(item_skill: ItemSkillUpdateDTO, request: Request, response: Response):
    try:
        item = await ItemService(request.app.state.db).update_skill(item_skill)
        if item is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return item
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_item(id: str, request: Request, response: Response):
    try:
        item = await ItemService(request.app.state.db).delete(id)
        if item is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return item
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
        