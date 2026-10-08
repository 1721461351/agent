import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.application.errors.exceptions import AppException
from app.interfaces.schemas import response

log = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI):
    ## 注意这里没有s
    @app.exception_handler(Exception)
    async def exception_handler(request: Request, e: Exception) -> JSONResponse:
        log.error(f"Exception: {str(e)}")
        return JSONResponse(status_code=500,
                            content=response.Response(code=500, message="服务器错误", data={}).model_dump()
                            )

    @app.exception_handler(HTTPException)
    async def exception_handler(request: Request, e: HTTPException) -> JSONResponse:
        log.error(f"Exception: {str(e)}")
        return JSONResponse(status_code=400,
                            content=response.Response(code=e.status_code, message="http异常", data={}).model_dump()
                            )

    @app.exception_handler(AppException)
    async def exception_handler(request: Request, e: AppException) -> JSONResponse:
        log.error(f"Exception: {str(e)}")
        return JSONResponse(status_code=e.status_code,
                            content=response.Response(code=e.status_code, message=e.msg, data={}).model_dump()
                            )
