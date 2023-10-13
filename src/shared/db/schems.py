from flask_marshmallow import fields
import marshmallow as ma_r
from src.crm_core.app_gen import ma, db
from src.shared.db.models import Order, Storage, Product


class StorageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Storage
        include_relationships = True

    count = ma.auto_field()
    place = ma.auto_field()


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
        include_relationships = True

    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    storage_info = ma.Nested(StorageSchema, many=True)


product_schema = ProductSchema(many=True)
