from flask import Flask, request, jsonify, session
from flask_session import Session
import os

app = Flask(__name__)

secret_key = os.getenv('SECRET_KEY', 'invalid_key')
session_type = os.getenv('SESSION_TYPE', 'invalid_type')
app.config["SECRET_KEY"] = secret_key
app.config["SESSION_TYPE"] = session_type
Session(app)

# Simulation of an in-memory user database
usuarios = {
    "7f20b9f6-9ff1-49f3-90e7-6f055a3c868a": {"nombre": "Usuario1", "email": "usuario1@example.com"},
    "1c8341a9-b0e6-47f4-9ded-6c67e2344d43": {"nombre": "Usuario2", "email": "usuario2@example.com"},
    "040200f3-c130-4274-af89-2fd1ce311aa4": {"nombre": "Usuario3", "email": "usuario3@example.com"},
}

# Simulation of authentication and session establishment
@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    session['user_id'] = user_id if user_id in usuarios else None
    if session['user_id'] is None:
        return "Usuario no encontrado", 404
    else:
        return "Login exitoso"

@app.route('/profile/<user_id>', methods=['GET'])
def ver_perfil(user_id):
    # Verification that the user is logged in
    if 'user_id' not in session:
        return "Usuario no autenticado", 401

    # Check permissions for the requested user ID
    if session['user_id'] != user_id:
        return "Acceso denegado", 403

    usuario = usuarios.get(user_id)
    if usuario:
        return jsonify(usuario)
    else:
        return "Usuario no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
