from sqlalchemy import (Column, MetaData, String, Table,
                        create_engine, DateTime)
from databases import Database
import os
DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

orders = Table(
    'orders',
    metadata,
    Column('order_id', String(250), primary_key=True),
    Column('created_on', DateTime),
    Column('status', String(50)),
    Column('customer_id', String(250)),
)

database = Database(DATABASE_URL)
