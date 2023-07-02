from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from canasu.config import LocalDevelopmentConfig
from canasu.database import db, ma
from canasu.api.auth import auth
from canasu.api.project import project_blueprint
from canasu.api.module import module_blueprint
from canasu.api.enrollment import enrollment
from canasu.api.mentor import mentor
from canasu.api.mentee import mentee
from canasu.api.admin import admin
from canasu.api.session import session
from canasu.api.mapping import mapping

def create_app(config_class=LocalDevelopmentConfig):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(admin)
    app.register_blueprint(auth)
    app.register_blueprint(enrollment)
    app.register_blueprint(mapping)
    app.register_blueprint(mentee)
    app.register_blueprint(mentor)
    app.register_blueprint(module_blueprint)
    app.register_blueprint(project_blueprint)
    app.register_blueprint(session)
    
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    JWTManager(app)
    
    
    with app.app_context():
        db.create_all() 
    return app
