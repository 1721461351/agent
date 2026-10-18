from fastapi import APIRouter

from app.interfaces.api import status_router, app_config_router


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(status_router.api_router)
    api_router.include_router(app_config_router.router)

    return api_router


myRouter = create_api_router()
