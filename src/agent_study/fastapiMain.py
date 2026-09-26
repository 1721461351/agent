from fastapi import FastAPI
#from typing import Union
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/app/{app_id}")
async def content(app_id: int, app_name: str):
    print(app_id, app_name)
    return {"app_id": app_id, "app_name": app_name}