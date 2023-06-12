from utils.database import db

from utils.database import Product as ProductDB, ProductSize as ProductSizes, ProductColor as ProductColors, SubCategories as SubCategoriesDB, Categories as CategoriesDB

def get_products(id:int=None, search_string:str=None, category_item:str=None, subcategory_item:str=None) -> list:
    products = []
    if id is None:
        # Get all products from db
        for product in db.session.query(ProductDB).all():
            subcategory = db.session.query(SubCategoriesDB).get(product.subcategory_id)
            subcategory_name = subcategory.name
            category = db.session.query(CategoriesDB).get(subcategory.category_id)
            category_name = category.name
            product_info = {'id': product.id,
                            'name': product.name, 
                            'image': product.image, 
                            'description': product.description,
                            'category_name': category_name,
                            'subcategory_name': subcategory_name}
            products.append(product_info)
        # Filter products for search action
        if search_string:
            if len(products):
                filterd_products = [product for product in products 
                                    if search_string.lower() in product["name"].lower() 
                                    or search_string.lower() in product["category_name"].lower()
                                    or search_string.lower() in product["subcategory_name"].lower()]
                products = filterd_products

        # If go by category, filter category & subcategory
        if subcategory_item and not search_string:
            if len(products):
                filterd_products = list(filter(lambda product : True 
                                               if product['subcategory_name'] == subcategory_item 
                                               and product['category_name'] == category_item
                                               else False, products))
                products = filterd_products
            
      
    else:
        product = db.session.query(ProductDB).get(id)
        sizes = product.sizes
        colors = product.colors
        product_info = {'id': product.id,
                        'name': product.name, 
                        'image': product.image, 
                        'description': product.description,
                        'stocks': product.stocks,
                        'price': product.price,
                        'material': product.material,
                        'composition': product.composition,
                        'care': product.care,
                        'exchange': product.exchange,
                        'country': product.country,
                        'sizes': [size.size for size in sizes],
                        'colors': [color.color for color in colors]}
        products.append(product_info)
    return products

def add_products(products):
    try:
        # Add to main product
        for product in products:
            # Add main product
            new_product = ProductDB(name=product['name'], 
                                    image=product['image'], 
                                    description=product['description'], 
                                    stocks=product['stocks'],
                                    price=product['price'],
                                    material=product['material'],
                                    composition=product['composition'],
                                    care=product['care'],
                                    exchange=product['exchange'],
                                    country=product['country'],
                                    subcategory_id=product['subcategory_id'])
            # Add size
            sizes = [ProductSizes(size=size) for size in product['sizes']]
            new_product.sizes.extend(sizes)
            # Add color
            colors = [ProductColors(color=color) for color in product['colors']]
            new_product.colors.extend(colors)
            db.session.add(new_product)
        db.session.commit()

    except Exception as e:
        print(e)
        return False 
    finally:
        db.session.close()

    return True


def delete_products(product_ids:list, is_delete_all:bool=False):
    if not is_delete_all:
        if not len(product_ids): return False
        products = db.session.query(ProductDB).filter(ProductDB.id.in_(product_ids)).all()
        try:
            for product in products:   
                ProductSizes.query.filter(ProductSizes.product_id == product.id).delete()
                ProductColors.query.filter(ProductColors.product_id == product.id).delete()
                db.session.delete(product)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            db.session.close()
    else:
        try:
            ProductSizes.query.delete()
            ProductColors.query.delete()
            counts = db.session.query(ProductDB).delete()
            db.session.commit()
            print(f'Deleted {counts} entries.')
        except Exception as e:
            print(e)
            return False
        finally:
            db.session.close()

    return True