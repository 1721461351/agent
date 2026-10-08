from fastapi import APIRouter

from app.interfaces.schemas.response import Response

api_router = APIRouter(prefix="/status", tags=["状态模块"])


@api_router.get(
    path="/",
    response_model=Response,
    description="检查数据库状态",
    summary="系统健康监测"
)
async def get_status() -> Response:
    return Response.success()
