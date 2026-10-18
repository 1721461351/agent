import logging
from functools import lru_cache

from app.application.service.app_config_service import AppConfigService
from app.base.storage.file_app_config_repository import FileAppConfigRepository
from core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


@lru_cache
def get_app_config_service() -> AppConfigService:
    """获取应用配置信息"""
    path = settings.app_config_filepath
    repository = FileAppConfigRepository(path)
    """实例化appconfigservice"""
    return AppConfigService(repository)
