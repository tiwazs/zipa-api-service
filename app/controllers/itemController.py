from fastapi import APIRouter, Request, Response, status

from ..models.itemDTO import ItemDTO, ItemUpdateDTO, ItemCreateDTO
from ..services.itemService import ItemService

router = APIRouter(prefix="/items", tags=["Items"])

msg_not_found = 'Item not found'

@router.get("/")
async def get_items(request: Request, response: Response):
    return await ItemService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_item_by_id(id: str, request: Request, response: Response):
    try:
        item = await ItemService(request.app.state.db).get_by_id(id)
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
    
@router.put("/{id}")
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
        