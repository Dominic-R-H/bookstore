from flask import Blueprint, render_template, request, session, url_for, redirect
import secrets

home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    logged_in = 'user_id' in session
    return render_template('home.html', logged_in=logged_in)

