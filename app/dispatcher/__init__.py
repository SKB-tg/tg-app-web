from fastapi import APIRouter, Request, Response

from .routes import router as content_router
from .gpt import router as gpt_router
from .endpoint_stor import router as storage_router

main_router = APIRouter()
#router_views = APIRouter()

main_router.include_router(content_router, prefix="/content", tags=["content"])
main_router.include_router(storage_router, prefix="/storage", tags=["storage"])
main_router.include_router(gpt_router, prefix="/gpt", tags=["gpt"])


@main_router.get("/status")
async def index(request: Request, response: Response):
	response=Response()
	print(response.status_code)
	try:
		return response.status_code, {"ok": f'Status code:  {response.status_code}'}
	except Exception as e:
		print(e, "Error")
		return response.status_code, {"ok": f'Status code:  {response.status_code}'}