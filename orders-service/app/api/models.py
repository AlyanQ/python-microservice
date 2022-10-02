from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class GetOrder(BaseModel):
    order_id: str
    created_on: datetime
    status: str
    customer_id: str

class PostOrder(BaseModel):
    status: str
    customer_id: str

class UpdateOrder(BaseModel):
    status: Optional[str] = None
    customer_id: Optional[str] = None

class DeleteOrder(BaseModel):
    order_id: str

class DisplayOrder(BaseModel):
    order_id: str
    created_on: datetime
    status: str
    customer_id: str