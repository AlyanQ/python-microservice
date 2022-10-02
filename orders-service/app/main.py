import time
from fastapi import FastAPI, Request
from fastapi_pagination import add_pagination

from app.api.db import metadata, database, engine
from app.api.orders import orders

metadata.create_all(engine)

app = FastAPI()
add_pagination(app)
app.include_router(orders, prefix='/api/v1/orders', tags=['orders'])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time)
    response.headers["X-Process-Time"] = f'{process_time:.2f} s'
    return response

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
