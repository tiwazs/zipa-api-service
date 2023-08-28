from typing import Optional
from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..services.unitGenService import UnitGenerationService

router = APIRouter(prefix="/unit_gen", tags=["Unit Generation"])

msg_not_found = 'Trait not found'

@router.get("/")
async def get_traits(request: Request, response: Response, sigma_divider: Optional[float] = 4):
    return UnitGenerationService().generate_unit(sigma_divider)