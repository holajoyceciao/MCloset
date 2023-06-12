from flask import request, render_template

from controllers import product_controller as controller
from models import product as model

from utils import api_result

@controller.route('/', methods=['GET'])
def get_products():
    product_id = request.args.get('id') if request.args.get('id') else None
    products = model.get_products(product_id)
    return render_template('product.html', data=products)
    # code = 200 if len(products) else 400
    # return api_result.status_result(status_code=code, data=products)
    
@controller.route('/', methods=['POST'])
# Add new data to DB
def add_products():
    data = request.get_json()
    products = data['products']
    code = 200 if model.add_products(products=products) else 400
    return api_result.status_result(status_code=code)

@controller.route('/', methods=['DELETE'])
def delete_products():
    data = request.get_json()
    product_ids = []
    try:
        product_ids = data['product_ids']
    except KeyError as e:
        print('No id given')
    
    code = 200 if model.delete_products(product_ids=product_ids, is_delete_all=True) else 400
    return api_result.status_result(status_code=code)

# def put(self):
#     data = request.get_json()
#     names = data['names']
#     code = 200 if self.__product.update(names=names) else 400
#     return api_result.status_result(status_code=code)


