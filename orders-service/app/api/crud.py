from datetime import datetime
from typing import List
from app.api.models import PostOrder, UpdateOrder, DisplayOrder
from app.api.db import database, orders


async def add_order(order_id: str, created_on: datetime, payload: PostOrder) -> DisplayOrder:
    
    query = orders.insert().values(
        order_id=order_id, created_on=created_on, **payload.dict())

    return await database.execute(query=query)


async def get_all_orders() -> List[DisplayOrder]:
    query = orders.select()
    return await database.fetch_all(query=query)


async def get_order(order_id: str) -> DisplayOrder:
    query = orders.select(orders.c.order_id == order_id)
    return await database.fetch_one(query=query)


async def delete_order(order_id: str) -> DisplayOrder:
    query = orders.delete().where(orders.c.order_id == order_id)
    return await database.execute(query=query)


async def update_order(order_id: str, payload: UpdateOrder) -> DisplayOrder:
    query = (
        orders
        .update()
        .where(orders.c.order_id == order_id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
