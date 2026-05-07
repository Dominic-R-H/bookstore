from flask import Blueprint, render_template, request, session, url_for, redirect, jsonify
from models import user_model
from models import book_model
import services.order_service as order_service

order = Blueprint('order', __name__)

@order.route('/api/order', methods=['POST'])
def place_order():

    user_id = session.get('user_id')

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()    
    book_id = data.get('book_id')    
    if not book_id:
        return jsonify({"error": "Missing book_id"}), 400

    order_id = order_service.place_order(user_id, book_id)
    if order_id:        
        return jsonify({'order_id': order_id}), 201
    else:
        return jsonify({"error": "Failed to place order"}), 500


@order.route('/api/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
        
    order = order_service.get_order_by_id(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
  
    return jsonify(order), 200

@order.route('/api/orders', methods=['GET'])
def get_orders():
        
    orders = order_service.get_orders()
    if orders is None:
        return jsonify({"error": "Internal server error"}), 500
    
    response = {
        "orders": orders
    }
    
    return jsonify(response), 200

