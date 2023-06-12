from flask import Blueprint

product_controller = Blueprint('product', __name__, url_prefix='/product')
category_controller = Blueprint('category', __name__, url_prefix='/category')
cart_controller = Blueprint('cart', __name__, url_prefix='/cart')
checkout_controller = Blueprint('checkout', __name__, url_prefix='/checkout')

from . import product
from . import category
from . import cart
from . import checkout