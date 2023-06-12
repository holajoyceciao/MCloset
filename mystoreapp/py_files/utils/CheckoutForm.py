from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

# form used in basket
class CheckoutForm(FlaskForm):

    firstname = StringField("NAME", validators=[InputRequired()])
    surname = StringField("SURNAME", validators=[InputRequired()])
    email = StringField("EMAIL", validators=[DataRequired(), Email()])
    phone = StringField("PHONE", validators=[InputRequired()])
    address = StringField("SHIPPING ADDRESS", validators=[InputRequired()])
    city = StringField("CITY", validators=[InputRequired()])
    state = SelectField("STATE", choices=[('QLD', 'QLD'), ('VIC', 'VIC'), ('NSW', 'NSW')], validators=[InputRequired()])
    postal_code = StringField("ZIP CODE", validators=[InputRequired()])
    cart = StringField("CART", validators=[InputRequired()])
    submit = SubmitField("Place Order")
    