from sqlalchemy.orm import relationship

from src.crm_core.app_gen import db
import enum
from src.shared.db.engine import engine, base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, UniqueConstraint
from src.shared.settings.config import postgres_db


class OrderStatus(enum.Enum):
    create = 1
    send = 2
    get = 3


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = (UniqueConstraint('name', 'price', name='unic_prod'), {'schema': postgres_db['schema']},)
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    storage_info = relationship("Storage", back_populates="prod_info")


class Storage(db.Model):
    __tablename__ = 'storage'
    __table_args__ = {'schema': postgres_db['schema']}
    __table_args__ = (UniqueConstraint('prod_id', 'place', name='unic_storage'), {'schema': postgres_db['schema']},)
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    prod_id = Column(Integer, ForeignKey(postgres_db['schema'] + '.' + Product.__tablename__ + '.id'))
    count = Column(Integer)
    place = Column(Integer)
    prod_info = relationship("Product", back_populates="storage_info")


class Order(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'schema': postgres_db['schema']}
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    phone_number = Column(String)
    address = Column(String)
    status = Column(Enum(OrderStatus))


class OrderItem(db.Model):
    __tablename__ = 'order_item'
    __table_args__ = (
        UniqueConstraint('order_id', 'product_id', name='unic_order_item'), {'schema': postgres_db['schema']},)
    order_id = Column(Integer, ForeignKey(postgres_db['schema'] + '.' + Order.__tablename__ + '.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey(postgres_db['schema'] + '.' + Product.__tablename__ + '.id'),
                        primary_key=True)
    cunt = Column(Integer)


if __name__ == "__main__":
    base.metadata.create_all(engine)
