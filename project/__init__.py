# project/__iniit__.py

import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# Instancia a aplicação
app = Flask(__name__)

# Define a configuração
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Instancia o banco de dados
db = SQLAlchemy(app)


# Modelo
class User(db.Model):
    __tableusers_ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now()


# Rotas
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
