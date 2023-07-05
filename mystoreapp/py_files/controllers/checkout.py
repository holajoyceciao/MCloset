import json
from flask import render_template, flash, redirect, url_for, request, jsonify
from utils import common
import stripe

from controllers import checkout_controller as controller
from models import checkout as model
# import env as app_env
import os

from utils import api_result
from utils.CheckoutForm import CheckoutForm

order_info = {}

@controller.route('/', methods=['GET'])
def get_checkout():
    form = CheckoutForm()
    parsed_cart = common.parse_cart()

    return render_template('checkout.html', cart=parsed_cart, form=form)
    # code = 200 if len(order_ids) else 400
    # return api_result.status_result(status_code=200, data=checkout)

@controller.route('/', methods=['POST'])
def add_checkout():
    global order_info
    form = CheckoutForm()

    if form.validate_on_submit():
        order_info = {
            'firstname': form.firstname.data,
            'surname': form.surname.data,
            'email': form.email.data,
            'phone': form.phone.data,
            'address': form.address.data,
            'city': form.city.data,
            'state': form.state.data,
            'postal_code': form.postal_code.data,
            'cart': json.loads(form.cart.data)
        }
        form.firstname.data = ''
        form.surname.data = ''
        form.email.data = ''
        form.phone.data = ''
        form.address.data = ''
        form.city.data = ''
        form.state.data = ''
        form.postal_code.data = ''
        return redirect(url_for('checkout.get_checkout', success='true'))
    
    return api_result.status_result(status_code=400)


@controller.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    domain = 'http://' + os.environ.get('SERVER_HOST') + ':' + os.environ.get('SERVER_PORT')
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    
    cart_items = request.get_json()['request']
    line_items = []
    for items in cart_items:
        line_item={
                    'price_data': {
                        'currency': 'aud',
                        'product_data': {
                            'name': items['product_name'] + ' ' + items['color'] + ' ' +'Size:' + items['size'] ,
                        },
                        'unit_amount': int(items['price'])*100,
                    },
                    'quantity': int(items['quantity']),
                },
        line_items.append(line_item)
    
    line_items_tuple = line_items
    line_items = [item[0] for item in line_items_tuple]

    try:
        # data from frontend 
        checkout_session = stripe.checkout.Session.create(
            success_url= domain + '/checkout/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= domain + '/checkout/cancel',
            payment_method_types=["card"],
            line_items=line_items,
            mode='payment',
        )
        return jsonify({"sessionId" : checkout_session["id"]})
    except Exception as e:
        print(e)
        return str(e)
    
@controller.route('/success', methods=['GET'])
def handle_checkout_success():
    code = 400
    session_id = request.args.get('session_id')
    if session_id:
        code = 200 if model.add_order(order_info) else 400

    return redirect(url_for('checkout.get_checkout', payment='paid'))