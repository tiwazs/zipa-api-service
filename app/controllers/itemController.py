from fastapi import APIRouter, Request, Response, status, File, UploadFile


from ..models.itemDTO import ItemDTO, ItemUpdateDTO, ItemCreateDTO
from ..models.itemSkillDTO import ItemSkillCreateDTO, ItemSkillUpdateDTO
from ..models.itemTraitDTO import ItemTraitCreateDTO, ItemTraitUpdateDTO
from ..services.itemService import ItemService

router = APIRouter(prefix="/items", tags=["Items"])

msg_not_found = 'Item not found'

@router.get("/")
async def get_items(request: Request, response: Response, include_skills: bool = True, include_traits: bool = True, by_type: str = None, by_rarity: str = None, by_name: str = None, by_description: str = None, by_skill: str = None, by_trait: str = None):
    return await ItemService(request.app.state.db).get_all(include_skills, include_traits, by_type, by_rarity)

@router.get("/{id}")
async def get_item_by_id(id: str, request: Request, response: Response, include_skills: bool = True, include_traits: bool = True):
    try:
        item = await ItemService(request.app.state.db).get_by_id(id, include_skills, include_traits)
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

@router.put("/add_trait/{id}")
async def add_trait_to_item(id: str, trait_id: str, request: Request, response: Response):
    try:
        race = await ItemService(request.app.state.db).add_trait(id, trait_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_trait/{id}")
async def remove_trait_from_item(id: str, trait_id: str, request: Request, response: Response):
    try:
        race = await ItemService(request.app.state.db).remove_trait(id, trait_id)
        if race is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return race
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

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await ItemService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}        