# project/__init__.py

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# Instancia o banco de dados
db = SQLAlchemy()


def create_app():
    # Instancia a aplicação
    app = Flask(__name__)

    # Define a configuração
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Define as extensões
    db.init_app(app)

    # Registra as blueprints
    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
