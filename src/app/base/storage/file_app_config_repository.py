import logging
from pathlib import Path
from typing import Optional

import yaml
from filelock import FileLock

from app.application.errors.exceptions import ServerRequestsError
from app.domain.models.app_config import AppConfig, LLMConfig
from app.domain.repositories.app_config_repository import AppConfigRepository

log = logging.getLogger(__name__)


class FileAppConfigRepository(AppConfigRepository):

    def __init__(self, file_path: str) -> None:
        # 获取当前项目的根目录
        root_dir = Path.cwd()

        # 拼接
        self._file_path = root_dir.joinpath(file_path)

        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock_file = self._file_path.with_suffix(".lock")  # 文件锁

    def _create_default_app_config_if_not_exists(self):
        """文件不存在，使用默认配置"""
        if not self._file_path.exists():
            default_app_config = AppConfig(
                llm_config=LLMConfig()
            )
            self.save(default_app_config)

    def load(self) -> Optional[AppConfig]:

        self._create_default_app_config_if_not_exists()

        try:
            with open(self._file_path, "r", encoding="utf-8") as fp:
                data = yaml.safe_load(fp)
                return AppConfig.model_validate(data)

        except Exception as e:
            log.error(f"读取配置文件失败，{str(e)}")
            raise ServerRequestsError("读取应用配置失败，请稍后重试")

    def save(self, app_config: AppConfig) -> None:
        """"将appconfig传入到本地文件中"""
        lock = FileLock(self._lock_file, timeout=5)

        try:
            with lock:
                # 将appconfig转成字典
                data_to_dump = app_config.model_dump(mode='json')

                # 打开yaml文件并写入
                with open(self._file_path, "w", encoding="utf-8") as fp:
                    yaml.dump(data_to_dump, fp, allow_unicode=True, sort_keys=False)
        except Exception as e:
            log.error(f"写入配置文件失败，{str(e)}")
            raise ServerRequestsError("写入配置文件失败，请稍后重试")
