from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(68), nullable=False, unique=True)
    image = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    stocks = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    material = db.Column(db.String(500), nullable=False)
    composition = db.Column(db.String(500), nullable=False)
    care = db.Column(db.String(500), nullable=False)
    exchange = db.Column(db.String(500), nullable=False)
    country = db.Column(db.String(60), nullable=False)
    subcategory_id = db.Column(db.Integer, nullable=False)
    sizes = db.relationship('ProductSize', backref='products', lazy=True, cascade="all, delete")
    colors = db.relationship('ProductColor', backref='products', lazy=True, cascade="all, delete")
    
class ProductSize(db.Model):
    __tablename__ = 'product_sizes'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    size = db.Column(db.String(20), nullable=False)

class ProductColor(db.Model):
    __tablename__ = 'product_colors'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    color = db.Column(db.String(20), nullable=False)

class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = name = db.Column(db.String(68), nullable=False, unique=True)
    
class SubCategories(db.Model):
    __tablename__ = 'subcategories'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    name = db.Column(db.String(68), nullable=False, unique=False)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    postal_code = db.Column(db.String(64), nullable=False)
    order_details = db.relationship('OrderDetails', backref='orders', lazy=True, cascade="all,delete")

class OrderDetails(db.Model):
    __tablename__ = 'order_details', 
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product_color = db.Column(db.String(20), nullable=False)
    product_price =  db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(64), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    product_size = db.Column(db.String(20), nullable=False)