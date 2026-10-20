from abc import ABC, abstractmethod
from typing import Protocol, Optional

from external.mesage_queue import MessageQueue


class TaskRunner(ABC):
    """任务运行器，负责任务的执行，关心的是如何执行任务，销毁任务释放资源"""

    @abstractmethod
    async def invoke(self, task: "Task") -> None:
        """调用并执行"""
        raise NotImplementedError

    @abstractmethod
    async def destory(self) -> None:
        """销毁任务，并释放资源，包括关闭网络链接，清理内容，后台进程等"""
        raise NotImplementedError

    @abstractmethod
    async def on_done(self, task: "Task") -> None:
        """执行任务完成后对应的回调函数"""
        raise NotImplementedError


class Task(Protocol):
    """定义任务相关的接口协议"""

    async def run(self) -> None:
        """运行当前任务"""
        ...

    async def cancel(self) -> None:
        """取消当前任务"""
        ...

    @property
    def input_stream(self) -> MessageQueue:
        """只读属性，返回任务的输入流"""
        ...

    @property
    def output_stream(self) -> MessageQueue:
        """只读属性，返回任务的输出流"""
        ...

    @property
    def id(self) -> str:
        """只读属性，返回id"""

    @property
    def done(self) -> bool:
        """只读属性，返回任务是否完成"""

    @classmethod
    def get(cls, task_id: str) -> Optional["Task"]:
        """类方法，根据任务id获取任务"""
        ...

    @classmethod
    def create(cls, task_runner: TaskRunner) -> "Task":
        """根据传递的任务运行器，创建任务"""
        ...
    
    @classmethod
    def destory(cls) -> None:
        """销毁所有的任务实例"""
        ...
