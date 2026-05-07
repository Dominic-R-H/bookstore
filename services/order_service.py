import models.order_model as order_model
import models.user_model as user_model
import models.book_model as book_model

def place_order(user_id, book_id):
    user = user_model.get_user_by_id(user_id)
    book = book_model.get_book_by_id(book_id)
    
    if not user or not book:
        return None
    
    return order_model.create_order(user['name'], user['email'], user['phone'], book['title'], book['price'])

def get_order_by_id(order_id):
    return order_model.get_order_by_id(order_id)

def get_orders():
    return order_model.get_orders()