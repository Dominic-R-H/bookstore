from flask import Flask
from controllers.auth_controller import auth
from controllers.home_controller import home
from controllers.books_controller import books
from controllers.order_controller import order
from controllers.manager_controller import manager

app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.secret_key = "sfskjflkjflkjflksjflkj374uoiewdhhakjh"


# Register the controllers
app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(books)
app.register_blueprint(order)
app.register_blueprint(manager)


if __name__ == '__main__':
    app.run(debug=True)

