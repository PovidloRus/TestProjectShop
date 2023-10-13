from sqlalchemy.orm import joinedload
from src.crm_core.app_gen import db
import sqlalchemy as sa
from src.shared.db.models import Product, Storage
from sqlalchemy.dialects.postgresql import insert

def update_prod(product_id, product):
    q = sa.update(Product).where(product_id=product_id).values(product)
    with db.session() as session:
        session.execute(q)
        session.commit()


def add_prod(products):
    # a = Address(email='foo@bar.com')
    # p = Person(name='foo', addresses=[a])
    prod_models_obj = []

    with db.session() as session:
        for i in products:
            q = insert(Product).values(name=i['name'], price=i['price']).on_conflict_do_update(
                constraint='unic_prod', set_=dict(name=i['name'], price=i['price'])).returning(Product.id)
            session.commit()
            product_id = session.execute(q).fetchone()

            for z in i['storage_info']:
                q = insert(Storage).values(prod_id=product_id.id, count=z['count'], place=z['place']).on_conflict_do_update(
                    constraint='unic_storage', set_=dict(prod_id=product_id.id, count=z['count'], place=z['place']))
                session.execute(q)
            session.commit()


def get_all_prod():
    q = sa.select(Product.name, Product.price, Storage.place, Storage.count).join(Storage,
                                                                                  Product.id == Storage.prod_id)
    with db.session() as session:
        resp = session.execute(q)
    return (resp.featchall())


def get_prod_by_id(prod_ids):
    q = db.select(Product).options(joinedload(Product.storage_info)).where(Product.id.in_(prod_ids))

    with db.session() as session:
        resp = session.execute(q).unique()
        return resp.fetchall()