import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.base.logging.logging import set_logging
from app.base.storage.postgres import get_postgres
from app.base.storage.redis import get_redis
from app.interfaces.api.router import myRouter
from app.interfaces.errors.exception_hanlder import register_exception_handlers
from core.config import get_settings

settings = get_settings()
print(settings)

set_logging()
logging = logging.getLogger(__name__)

logging.info("日志打印")

api_tag = [
    {
        "name": "监测模块",
        "description": "监测服务状态"
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logging.info("生命周期开始yield前")
        await get_redis().init()
        await  get_postgres().init()
        yield
        logging.info("生命周期开始yield后")

    finally:
        await get_redis().shutdown()
        await get_postgres().shutdown()
        logging.info("生命周期结束")


app = FastAPI(title="ai系统",
              description="agent智能体",
              version="0.0.1",
              api_tags=api_tag,
              lifespan=lifespan
              )

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

register_exception_handlers(app)
app.include_router(myRouter, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# uvicorn app.main:app
