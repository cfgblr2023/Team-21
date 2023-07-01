from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from canasu.config import LocalDevelopmentConfig
from canasu.database import db, ma

# from canasu.api import register_api

def create_app(config_class=LocalDevelopmentConfig):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    JWTManager(app)
    
    
    with app.app_context():
        db.create_all() 
    return app
