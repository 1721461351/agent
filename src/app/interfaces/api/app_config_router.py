import logging

from fastapi import APIRouter
from fastapi.params import Depends

from app.application.service.app_config_service import AppConfigService
from app.base.service_dependencies import get_app_config_service
from app.domain.models.app_config import LLMConfig
from app.interfaces.schemas.response import Response

log = logging.getLogger(__name__)
router = APIRouter(
    prefix="/app-config",
    tags=["设置模块"]
)


@router.get(path="/llm", response_model=Response[LLMConfig], summary="获取配置信息",
            description="获取模型提供商提供的参数")
async def get_llm_config(
        app_config_service: AppConfigService = Depends(get_app_config_service)
) -> Response[LLMConfig]:
    llm_config = await app_config_service.get_llm_config()
    return Response.success(data=llm_config.model_dump(exclude={"api_key"}))


@router.post(path="/llm", response_model=Response[LLMConfig], summary="更新配置信息",
             description="更新llm配置，当apikey不为空的时候更新")
async def update_llm_config(
        llm_config: LLMConfig,
        app_config_service: AppConfigService = Depends(get_app_config_service)
):
    new_llm_config = await app_config_service.update_llm_config(llm_config)

    return Response.success(data=new_llm_config.model_dump(exclude={"api_key"}), msg="更新成功")
