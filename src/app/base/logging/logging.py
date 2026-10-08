import logging
import sys

from core.config import get_settings


def set_logging():
    ## 获取日志配置
    settings = get_settings()
    logLevel = settings.log_level

    # 获取根日志次处理器
    root = logging.getLogger()

    # 设置日志登记
    root.setLevel(logLevel)

    # 打印到控制台
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    handler.setLevel(logLevel)
    root.addHandler(handler)

    logging.warning("日志初始化完成")
