#this init.py file makes this website folder a python package
#whenever you keep __init__ file inside a folder, the folder becomes a package

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "ajdkfjaiudjhfadjfadkf" #encrypt cookies and session data related to the website


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app