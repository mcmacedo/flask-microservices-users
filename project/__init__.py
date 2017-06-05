# project/__iniit__.py

import os
from flask import Flask, jsonify


# Instancia da aplicação
app = Flask(__name__)

# Define a configuração
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
