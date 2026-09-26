from typing import TypeVar, Generic, Optional

from pydantic import BaseModel, Field

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    code: int = 200
    message: str = "success"
    data: Optional[T] = Field(default_factory=dict)  # 响应数据默认为空字典

    @staticmethod
    def success(msg: str = "success", data: Optional[T] = None) -> "Response[T]":
        """成功消息，code固定为200，携带msg和data"""
        return Response(code=200, message=msg, data=data if data else {})

    @staticmethod
    def fail(code: int, msg: str, data: Optional[T] = None) -> "Response[T]":
        """失败消息提示，携带code/msg/data"""
        return Response(code=code, message=msg, data=data if data else {})
