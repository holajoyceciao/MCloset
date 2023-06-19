import json
from flask import render_template, flash, redirect, url_for, request, jsonify
from utils import common
import stripe

from controllers import checkout_controller as controller
from models import checkout as model
import env as app_env

from utils import api_result
from utils.CheckoutForm import CheckoutForm

@controller.route('/', methods=['GET'])
def get_checkout():
    form = CheckoutForm()
    parsed_cart = common.parse_cart()

    return render_template('checkout.html', cart=parsed_cart, form=form)
    # code = 200 if len(order_ids) else 400
    # return api_result.status_result(status_code=200, data=checkout)

@controller.route('/', methods=['POST'])
def add_checkout():
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
        code = 200 if model.add_order(order_info) else 400
        form.firstname.data = ''
        form.surname.data = ''
        form.email.data = ''
        form.phone.data = ''
        form.address.data = ''
        form.city.data = ''
        form.state.data = ''
        form.postal_code.data = ''
        flash('Form submitted successfully.')
        return redirect(url_for('checkout.get_checkout', success='true'))
    
    return api_result.status_result(status_code=400)


@controller.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    domain = 'http://' + app_env.SERVER_HOST + ':' + app_env.SERVER_PORT
    stripe.api_key = app_env.STRIPE_SECRET_KEY
    try:
        # data from frontend 
        checkout_session = stripe.checkout.Session.create(
            success_url= domain + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= domain + '/cancel',
            payment_method_types=["card"],
            line_items=[{
                'price_data': {
                    'currency': 'aus',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': 90000,
                },
                'quantity': 1,
            },
        ],
            mode='payment',
        )
        return jsonify({"sessionId" : checkout_session["id"]})
    except Exception as e:
        return str(e)
