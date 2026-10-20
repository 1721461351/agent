from typing import Protocol, Any, Tuple


class MessageQueue(Protocol):
    """消息队列协议"""

    async def add(self, message:Any) -> str:
        """添加一条消息，返回对应的消息id"""
        ...

    async def get(self, start_id:str = None,block_ms:int = None) -> Tuple[str, Any]:
        """根据传递的开始时间id和阻塞时间，获取一条消息"""
        ...

    async def pop(self) -> Tuple[str, Any]:
        """获取并移除最新的一条消息"""

        ...

    async def clear(self) -> None:
        """"清空消息队列中的所有消息"""
        ...

    async def is_empty(self) -> bool:
        """判断消息队列是否为空"""
        ...

    async def size(self) -> int:
        """获取消息队列的长度"""
        ...

    async def delete_message(self, message_id:str) -> bool:
        """根据传递的消息id删除指定的消息"""
        ...