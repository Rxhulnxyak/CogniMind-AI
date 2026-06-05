from fastapi import APIRouter
from . import chat, memory, knowledge

router = APIRouter()

router.include_router(chat.router, prefix="/chat", tags=["chat"])
router.include_router(memory.router, prefix="/memory", tags=["memory"])
router.include_router(knowledge.router, prefix="/knowledge", tags=["knowledge"])
