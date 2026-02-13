from email import message
from fastapi import APIRouter
from .incidents import router as incidents_router

router = APIRouter()
router.include_router(incidents_router)
