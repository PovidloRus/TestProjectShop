import marshmallow as ma_r
from src.crm_core.app_gen import ma, db


class GetIdValid(ma.Schema):
    ids = ma_r.fields.List(ma_r.fields.Integer(many = True))


get_id_valid = GetIdValid()
