from typing import Optional
from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..services.unitGenService import UnitGenerationService

router = APIRouter(prefix="/unit_gen", tags=["Unit Generation"])

msg_not_found = 'Trait not found'

@router.get("/")
async def get_unit_values(request: Request, response: Response, sigma_divider: Optional[float] = 4):
    return UnitGenerationService().generate_unit(sigma_divider)

@router.get("/single_value")
async def get_unit_value(request: Request, response: Response, start: int, end: int, sigma_divider: Optional[float] = 4):
    return UnitGenerationService().gaussian_random_in_range(start, end, sigma_divider)