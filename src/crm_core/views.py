import marshmallow

from src.crm_core.app_gen import app
from flask import request, jsonify
from src.shared.db.queryes.api_queryes import add_prod, get_prod_by_id
from src.shared.db.schems import product_schema
from validate.validator import get_id_valid


@app.route('/product', methods=['GET', 'POST', 'PUT'])
def get_product():
    request_data = request.get_json()
    if request.method == 'PUT':
        data = request.get_json()
        data = product_schema.load(data)
        add_prod(data)
        return jsonify(True)

    elif request.method == 'GET':
        request_data = request.get_json()
        try:
            data = get_id_valid.load(request_data)
        except marshmallow.exceptions.ValidationError as e:
            return e.messages
        prod_info = get_prod_by_id(data['ids'])
        prod_info =  [value for value, in prod_info]
        res = product_schema.dump(prod_info)
        return jsonify(res)



