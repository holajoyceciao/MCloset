from flask import request, render_template

from controllers import category_controller as controller
from models import category as model

from utils import api_result

@controller.route('/', methods=['GET'])
def get_categories():
    category_id = request.args.get('id') if request.args.get('id') else None
    categories = model.get_categories(category_id)
    code = 200 if len(categories) else 400
    return api_result.status_result(status_code=code, data=categories)
    
@controller.route('/', methods=['POST'])
# Add new data to DB
def add_categories():
    data = request.get_json()
    categories = data['categories']
    subcategories = data['subcategories']
    code = 200 if model.add_categories(categories=categories, subcategories=subcategories) else 400
    return api_result.status_result(status_code=code)

@controller.route('/', methods=['DELETE'])
def delete_categories():
    data = request.get_json()
    category_ids = []
    try:
        category_ids = data['category_ids']
    except KeyError as e:
        print('No id given')
    
    code = 200 if model.delete_categories(category_ids=category_ids, is_delete_all=True) else 400
    return api_result.status_result(status_code=code)