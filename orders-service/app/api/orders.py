from fastapi import APIRouter, HTTPException
from uuid import uuid4
from datetime import datetime
from fastapi_pagination import add_pagination, paginate, LimitOffsetPage

from app.api.models import PostOrder, UpdateOrder, DisplayOrder
from app.api import crud

orders = APIRouter()

@orders.get('/', response_model=LimitOffsetPage[DisplayOrder])
async def get_all_orders():
    return paginate(await crud.get_all_orders())

# Add a new order
@orders.post('/', response_model=DisplayOrder)
async def add_new_order(payload: PostOrder):
    order_id = str(uuid4())
    created_on = datetime.now()

    await crud.add_order(order_id, created_on, payload)

    response = {
        'order_id': order_id,
        'created_on': created_on,
        **payload.dict()
    }
    return response

# Get a single order
@orders.get('/{order_id}', response_model=DisplayOrder)
async def get_single_order(order_id: str):
    order = await crud.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return order

# Update an order
@orders.put('/{order_id}', response_model=DisplayOrder)
async def update_order(order_id: str, payload: UpdateOrder):
    order = await crud.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')

    update_data = payload.dict(exclude_unset=True)
    movie_in_db = DisplayOrder(**order)
    updated_order = movie_in_db.copy(update=update_data)

    await crud.update_order(order_id, updated_order)

    return updated_order

# Delete an order
@orders.delete('/{order_id}')
async def delete_order(order_id: str):
    order = await crud.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    await crud.delete_order(order_id)
    return order

add_pagination(orders)
