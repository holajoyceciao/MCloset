from flask import request, render_template

from controllers import cart_controller as controller
from utils import common

from utils import api_result

@controller.route('/', methods=['GET'])
def get_cart():
    parsed_cart = common.parse_cart()
    return render_template('shoppingcart.html', cart=parsed_cart)
    # code = 200 if len(cart_ids) else 400
    # return api_result.status_result(status_code=code, data=cart)
