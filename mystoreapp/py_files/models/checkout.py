from utils.database import Order as OrderDB, OrderDetails as OrderDetailsDB, db

def add_order(order_info:dict) -> bool:
    try:
        new_order = OrderDB(firstname=order_info['firstname'],
                            surname = order_info['surname'],
                            email = order_info['email'],
                            phone = order_info['phone'],
                            address = order_info['address'],
                            city = order_info['city'],
                            state = order_info['state'],
                            postal_code = order_info['postal_code'])
        products = [OrderDetailsDB(product_id=product['product_id'],
                                   product_color=product['color'],
                                   product_price=product['price'],
                                   product_name=product['product_name'],
                                   product_quantity=product['quantity'],
                                   product_size=product['size']) for product in order_info['cart']]
        new_order.order_details.extend(products)
        db.session.add(new_order)
        db.session.commit()


    except Exception as e:
        print(e)
        return False 
    finally:
        db.session.close()

    return True
