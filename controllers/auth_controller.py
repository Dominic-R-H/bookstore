from services import auth_service
from flask import Blueprint, render_template, request, session, url_for, redirect
import secrets

auth = Blueprint('auth', __name__)

CAPTCHA_FOLDER = "static/captcha"

def prepare_registration_page(error = None):
    # generate a CSRF Token
    csrf_token = secrets.token_hex(16)

    # Store the CSRF token in the session variable. 
    # This will be later visible when we do post request to ./login
    session['csrf_token'] = csrf_token
    
    return render_template(
        'register.html',
        error=error,
        csrf_token=csrf_token,
    )

def prepare_login_page(error = None):
    # generate a CSRF Token
    csrf_token = secrets.token_hex(16)
    
    # Select a random captcha file and its corresponding captcha code
    captcha_file, captcha_code = auth_service.get_random_captcha(CAPTCHA_FOLDER)

    # Store the CSRF token in the session variable. 
    # This will be later visible when we do post request to ./login
    session['csrf_token'] = csrf_token
    
    # Store the captcha code in the session variable. 
    # This will be later visible when we do post request to ./login
    session['captcha'] = captcha_code

    return render_template(
        'login.html',
        error=error,
        csrf_token=csrf_token,
        captcha_image=f"/static/captcha/{captcha_file}"
    )
    
@auth.route('/register', methods=['GET'])
def register_page():
    return prepare_registration_page()

@auth.route('/login', methods=['GET'])
def login_page():
    return prepare_login_page()

@auth.route('/login', methods=['POST'])
def login():
    """
    Our login post request needs to verify these things. 
    1. CSRF Token
    2. Form contents are valid
    3. Captcha Code is calid
    4. User exists and password is correct
    
    we will not expose if the user email is valid or not or if the password is correct or not.
    We will just say "Invalid credentials" if any of the above checks fail. 
    This is to prevent user enumeration attacks.
    """
    
    csrf_token = session.get('csrf_token')   
    form_csrf_token = request.form.get('csrf_token')
    
    # verify csrf token
    if not csrf_token or not form_csrf_token or csrf_token != form_csrf_token:
        return prepare_login_page(error="Session Expired")
    
    # verify form contents
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email or not password:
        return prepare_login_page(error="Invalid credentials")

    # verify captcha
    captcha = session.get('captcha')    
    form_captcha = request.form.get('captcha')

    if not captcha or not form_captcha or captcha != form_captcha:
        return prepare_login_page(error="Invalid captcha")

    # verify valid user
    user = auth_service.verify_user(email, password)
    if not user:
        return prepare_login_page(error="Invalid credentials")
    
    # set user session
    session['user_id'] = user['id']

    return redirect('/')


@auth.route('/register', methods=['POST'])
def register():
    """
    Our register post request needs to do these things.
    1. CSRF Token
    2. Form contents are valid
    3. User with the same email does not already exist
    4. Create the user and store in database
    5. Redirect to login page
    """
    csrf_token = session.get('csrf_token')   
    form_csrf_token = request.form.get('csrf_token')

    print("OKAY 2")
    
    # verify csrf token
    if not csrf_token or not form_csrf_token or csrf_token != form_csrf_token:
        return prepare_registration_page(error="Session Expired")
    
    print("OKAY 1")
    
    # verify form contents
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    password = request.form.get('password')

    if not auth_service.validate_registration_form(name, phone, email, password):
        return prepare_registration_page(error="Invalid form contents")

    print("OKAY 2")
    
    # verify if the user already exists
    if auth_service.email_exists(email):
        return prepare_registration_page(error="Email already taken")

    # register the user
    if not auth_service.register_user(name, phone, email, password):
        return prepare_registration_page(error="Registration failed")

    print("OKAY 3")
    
    return redirect(url_for('auth.login_page'))

@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('auth.login_page'))
