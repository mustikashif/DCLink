from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mustafa2005'

    @app.route("/")
    def home():
        return "<h1>123</h1>"

    return app