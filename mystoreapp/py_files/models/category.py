from utils.database import db

from utils.database import Categories as CategoriesDB, SubCategories as SubCategoriesDB

def get_categories(id:int=None) -> list:
    categories = []
    if id is None:
        for category in db.session.query(CategoriesDB).all():
            category_info = {'id': category.id,
                             'name': category.name,
                             'subcategories': []}
            categories.append(category_info)
        for subcategory in db.session.query(SubCategoriesDB).all():
            subcategory_info = {'id': subcategory.id,
                                'name': subcategory.name,
                                'category_id': subcategory.category_id}
            for category in categories:
                if category['id'] == subcategory_info['category_id']:
                    category['subcategories'].append(subcategory_info)

    else:
        category = db.session.query(CategoriesDB).get(id)
        category_info = {'id': category.id,
                         'name': category.name}
        categories.append(category_info)
    return categories

def add_categories(categories:list=[], subcategories:list=[]) -> bool:
    try:
        for category in categories:
            category = CategoriesDB(name=category)
            db.session.add(category)
        if len(subcategories):
            for subcategory in subcategories:
                subcategory = SubCategoriesDB(name= subcategory['name'], category_id=subcategory['category_id'])
                db.session.add(subcategory)
        db.session.commit()

    except Exception as e:
        print(e)
        return False 
    finally:
        db.session.close()

    return True


def delete_categories(category_ids:list, is_delete_all:bool=False):
    if not is_delete_all:
        if not len(category_ids): return False
        categories = db.session.query(CategoriesDB).filter(CategoriesDB.id.in_(category_ids)).all()
        try:
            for category in categories:
                SubCategoriesDB.query.filter(SubCategoriesDB.category_id == category.id).delete()
                db.session.delete(category)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        finally:
            db.session.close()
    else:
        try:
            SubCategoriesDB.query.delete()
            counts = db.session.query(CategoriesDB).delete()
            db.session.commit()
            print(f'Deleted {counts} entries.')
        except Exception as e:
            print(e)
            return False
        finally:
            db.session.close()

    return True




# def update(self, names:list):
#     for name in names:
#         old_name = name['old_name']
#         new_name = name['new_name']
#         try:
#             product_to_update = db.session.query(ProductDB).filter(ProductDB.name == old_name)
#             product_to_update.update({ProductDB.name: new_name}, synchronize_session=False)
#             db.session.commit()
#         except Exception as e:
#             print(e)
#             return False
#         return True

# def delete(self, names:list, is_delete_all:bool=False) -> bool:
#     if not is_delete_all:
#         products = db.session.query(ProductDB).filter(ProductDB.name.in_(names)).all()
#         try:
#             for product in products:   
#                 db.session.delete(product)
#             db.session.commit()
#         except Exception as e:
#             print(e)
#             return False
#         finally:
#             db.session.close()
#     else:
#         try:
#             counts = db.session.query(ProductDB).delete()
#             db.session.commit()
#             print(f'Deleted {counts} entries.')
#         except Exception as e:
#             print(e)
#             return False
#         finally:
#             db.session.close()

#     return True