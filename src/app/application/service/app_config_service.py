from typing import Optional

from app.domain.models.app_config import AppConfig, LLMConfig
from app.domain.repositories.app_config_repository import AppConfigRepository


class AppConfigService:

    def __init__(self, app_config_repo: AppConfigRepository) -> None:
        self._app_config_repo = app_config_repo

    async def _load_app_config(self) -> Optional[AppConfig]:
        """加载获取所有的应用配置"""
        return self._app_config_repo.load()

    async def get_llm_config(self) -> LLMConfig:
        """获取LLM提供商配置"""
        app_config = await self._load_app_config()
        return app_config.llm_config

    async def update_llm_config(self, llm_config: LLMConfig) -> LLMConfig:
        """根据传递的llm_config更新语言模型提供商配置"""
        # 1.获取应用配置
        app_config = await self._load_app_config()

        # 2.判断api_key是否为空
        if not llm_config.api_key.strip():
            llm_config.api_key = app_config.llm_config.api_key

        # 3.调用函数更新app_config
        app_config.llm_config = llm_config
        self._app_config_repo.save(app_config)

        return app_config.llm_config
