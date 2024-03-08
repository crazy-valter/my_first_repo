from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Simulation of an in-memory user database
usuarios = {
    "1": {"nombre": "Usuario1", "email": "usuario1@example.com"},
    "2": {"nombre": "Usuario2", "email": "usuario2@example.com"},
    "3": {"nombre": "Usuario3", "email": "usuario3@example.com"},
}


@app.route("/profile/<user_id>", methods=["GET"])
def ver_perfil(user_id):
    # No permissions check for the requested user ID
    usuario = usuarios.get(user_id)
    if usuario:
        return jsonify(usuario)
    else:
        return "Usuario no encontrado", 404


if __name__ == "__main__":
    app.run(debug=True)
