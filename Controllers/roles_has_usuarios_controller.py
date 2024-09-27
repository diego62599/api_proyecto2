from flask import Blueprint, request, jsonify
from models import db
from models.roles_has_usuarios import Roles_has_Usuarios
from flask_jwt_extended import jwt_required, get_jwt_identity


roles_has_usuarios_bp = Blueprint('roles_has_usuarios_bp', __name__)

@roles_has_usuarios_bp.route('/roles_has_usuarios', methods=['GET'])
@jwt_required()
def get_roles_has_usuarios():
    roles_has_usuarios = Roles_has_Usuarios.query.all()
    return jsonify([rol_has_usuario.to_dict() for rol_has_usuario in roles_has_usuarios]), 200

@roles_has_usuarios_bp.route('/roles_has_usuarios/<int:roles_id>/<int:usuarios_id>', methods=['GET'])
@jwt_required()
def get_rol_has_usuario(roles_id, usuarios_id):
    rol_has_usuario = Roles_has_Usuarios.query.get_or_404((roles_id, usuarios_id))
    return jsonify(rol_has_usuario.to_dict()), 200

@roles_has_usuarios_bp.route('/roles_has_usuarios', methods=['POST'])
def create_rol_has_usuario():
    data = request.get_json()
    new_rol_has_usuario = Roles_has_Usuarios(
        roles_id=data.get('roles_id'),
        usuarios_id=data.get('usuarios_id')
    )
    db.session.add(new_rol_has_usuario)
    db.session.commit()
    return jsonify(new_rol_has_usuario.to_dict()), 201

@roles_has_usuarios_bp.route('/roles_has_usuarios/<int:roles_id>/<int:usuarios_id>', methods=['DELETE'])
def delete_rol_has_usuario(roles_id, usuarios_id):
    rol_has_usuario = Roles_has_Usuarios.query.get_or_404((roles_id, usuarios_id))
    db.session.delete(rol_has_usuario)
    db.session.commit()
    return jsonify({'message': 'Rol_has_usuario eliminado'}), 200
