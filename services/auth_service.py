from werkzeug.security import check_password_hash, generate_password_hash
import models.user_model as user_model
import random
import os
import re


def get_random_captcha(captcha_folder):
    # pick a random captcha file from the captcha folder
    files = os.listdir(captcha_folder)
    captcha_file = random.choice(files)

    # extract captcha code from the filename
    # filename format: CAPTCHA_<number>_<captcha_code>.png
    captcha_code = captcha_file.split('.')[0].split('_')[-1]

    return captcha_file, captcha_code


def verify_user(email, password):
    
    user = user_model.get_user_by_email(email)
    
    if not user:
        return None
    
    if not check_password_hash(user['password'], password):
        return None

    return user


def validate_registration_form(name, phone, email, password):

    if not name or not re.match(r'^[A-Za-z\s]+$', name):
        return False
    
    if not phone or not phone.isdigit() or len(phone) != 10:
        return False
  
    if not email or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return False
    
    if not password or len(password) < 8:
        return False
    
    return True


def register_user(name, phone, email, password):
    hashed_password = generate_password_hash(password)
    return user_model.create_user(name, phone, email, hashed_password)


def email_exists(email):
    user = user_model.get_user_by_email(email)
    return user is not None
    