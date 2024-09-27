from flask import Blueprint, request, jsonify
from models import db
from models.roles import Roles
import logging  # Asegúrate de importar logging
roles_bp = Blueprint('roles_bp', __name__)
from flask_jwt_extended import jwt_required, get_jwt_identity


@roles_bp.route('/roles', methods=['GET'])
# @jwt_required()
def get_roles():
    try:
        roles = Roles.query.all()
        roles_list = [rol.to_dict() for rol in roles]
        return jsonify({
            "message": "Roles listados correctamente",
            "estado": 200,
            "roles": roles_list
        }), 200
    except Exception as e:
        logging.error("Error al obtener roles: %s", str(e))
        return jsonify({"message": "Error al obtener roles", "estado": 500}), 500


@roles_bp.route('/roles/<int:id>', methods=['GET'])
@jwt_required()
def get_rol(id):
    rol = Roles.query.get_or_404(id)
    return jsonify(rol.to_dict()), 200




@roles_bp.route('/roles', methods=['POST'])
def create_rol():
    data = request.get_json()
    new_rol = Roles(
        id=data.get('id'),
        nombre=data.get('nombre'),
        estado=data.get('estado')
    )
    db.session.add(new_rol)
    db.session.commit()
    return jsonify(new_rol.to_dict()), 201

@roles_bp.route('/roles/<int:id>', methods=['PUT'])
def update_rol(id):
    rol = Roles.query.get_or_404(id)
    data = request.get_json()
    rol.nombre = data.get('nombre', rol.nombre)
    rol.estado = data.get('estado', rol.estado)
    db.session.commit()
    return jsonify(rol.to_dict()), 200

@roles_bp.route('/roles/<int:id>', methods=['DELETE'])
def delete_rol(id):
    rol = Roles.query.get_or_404(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify({'message': 'Rol eliminado'}), 200
