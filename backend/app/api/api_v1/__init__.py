from core.config import settings
from .incidents import router as incidents_router

from fastapi import APIRouter

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(incidents_router)
