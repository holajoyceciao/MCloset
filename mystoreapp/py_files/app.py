from flask import Flask, render_template, request
from utils.database import db
import os
import stripe

from controllers import product_controller, category_controller, cart_controller, checkout_controller
from models import product as product_model, category as category_model
from utils import api_result as app_result

# import env as app_env

# intialization
app = Flask(__name__, static_folder='../static', template_folder='../templates')

# configuration of DB
cwd = os.getcwd()
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'instance', 'mcloset.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
# app.config['SECRET_KEY'] = app_env.SECRET_KEY
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
db.init_app(app)

# create DB
with app.app_context():
    db.create_all()

# This is your test secret API key.
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

# ---------------------------------------------------------------------------------------------------------- #

# homepage api
@app.route('/')
@app.route('/<path:path>')
def render_homepage(path=None):
    search_string = request.args.get('search') if request.args.get('search') else None
    category_item = request.args.get('category') if request.args.get('category') else None
    subcategory_item = request.args.get('subcategory') if request.args.get('subcategory') else None
    products = product_model.get_products(search_string=search_string, category_item=category_item, subcategory_item=subcategory_item) if product_model.get_products(search_string=search_string, category_item=category_item, subcategory_item=subcategory_item) and len(product_model.get_products(search_string=search_string, category_item=category_item, subcategory_item=subcategory_item)) else []
    categories = category_model.get_categories() if category_model.get_categories() and len(category_model.get_categories()) else []
    return render_template('homepage.html', products=products, categories=categories)

# ---------------------------------------------------------------------------------------------------------- #

# error handling 
@app.errorhandler(401)
def method_401(e):
    return app_result.status_result(status_code=401)

@app.errorhandler(403)
def method_403(e):
    return app_result.status_result(status_code=403)

@app.errorhandler(404)
def method_404(e):
    return app_result.status_result(status_code=404, description='requested URL was not found on the server')

@app.errorhandler(405)
def method_405(e):
    return app_result.status_result(status_code=405, description='http method is not allowed for the requested URL')

# ---------------------------------------------------------------------------------------------------------- #

# register blueprint
app.register_blueprint(product_controller)
app.register_blueprint(category_controller)
app.register_blueprint(cart_controller)
app.register_blueprint(checkout_controller)

# ---------------------------------------------------------------------------------------------------------- #

# run app
def run_app():
    app.run(host=os.environ['SERVER_HOST'], port=os.environ['SERVER_PORT'], debug=os.environ['SERVER_DEBUG'])

if __name__ == '__main__':
    run_app()