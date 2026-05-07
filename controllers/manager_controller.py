from flask import Blueprint, render_template, request, session, url_for, redirect, jsonify
from models import user_model
from models import book_model
import services.order_service as order_service

manager = Blueprint('manager', __name__)

@manager.route('/manager', methods=['GET'])
def manager_page():
    logged_in = 'user_id' in session
    return render_template('manager.html', logged_in=logged_in)

