from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# instantiate db
db = SQLAlchemy()

def create_app(script_info=None):
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    login = LoginManager(app)

    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app

