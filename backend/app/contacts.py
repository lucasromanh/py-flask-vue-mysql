from flask import Flask, Blueprint, request, jsonify
from app import app
from db import mysql

contacts = Blueprint('usuarios', __name__)

@contacts.route('/usuarios', methods=['GET'])
def get_usuarios():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data = cur.fetchall()
    cur.close()

    usuarios = []
    for row in data:
        usuario = {
            'id': row.get('id'),
            'nombre_completo': row.get('nombre_completo'),
            'telefono': row.get('telefono'),
            'email': row.get('email')
        }
        usuarios.append(usuario)

    return jsonify(usuarios)

@contacts.route('/usuarios', methods=['POST'])
def add_usuario():
    nombre_completo = request.json['nombre_completo']
    telefono = request.json['telefono']
    email = request.json['email']
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO usuarios (nombre_completo, telefono, email) VALUES (%s,%s,%s)",
            (nombre_completo, telefono, email))
        mysql.connection.commit()
        nuevo_usuario_id = cur.lastrowid
        cur.close()
        return jsonify({'id': nuevo_usuario_id, 'message': 'Usuario agregado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)})

@contacts.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    data = cur.fetchone()
    cur.close()
    if data:
        usuario = {
            'id': data['id'],
            'nombre_completo': data['nombre_completo'],
            'telefono': data['telefono'],
            'email': data['email']
        }
        return jsonify(usuario)
    else:
        return jsonify({'message': 'Usuario no encontrado'})

@contacts.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    nombre_completo = request.json.get('nombre_completo')
    telefono = request.json.get('telefono')
    email = request.json.get('email')
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE usuarios
        SET nombre_completo = %s,
            email = %s,
            telefono = %s
        WHERE id = %s
    """, (nombre_completo, email, telefono, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Usuario actualizado correctamente'})


@contacts.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = %s', (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Usuario eliminado correctamente'})