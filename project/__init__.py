# project/__iniit__.py

from flask import Flask, jsonify


# Instancia da aplicação
app = Flask(__name__)

# Define a configuração
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
