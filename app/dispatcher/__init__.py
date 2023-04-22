from fastapi import APIRouter

from .routes import router as content_router
from .gpt import router as gpt_router
from .endpoint_stor import router as storage_router

main_router = APIRouter()
#router_views = APIRouter()

main_router.include_router(content_router, prefix="/content", tags=["content"])
main_router.include_router(storage_router, prefix="/storage", tags=["storage"])
main_router.include_router(gpt_router, prefix="/gpt", tags=["gpt"])


# @main_router.get("/")
# async def index():
#     return {"message": "Hello World!"}