from flask import Blueprint, request, jsonify
from models import db
from models.roles_has_permisos import Roles_has_Permisos
from flask_jwt_extended import jwt_required, get_jwt_identity


roles_has_permisos_bp = Blueprint('roles_has_permisos_bp', __name__)

@roles_has_permisos_bp.route('/roles_has_permisos', methods=['GET'])
@jwt_required()
def get_roles_has_permisos():
    roles_has_permisos = Roles_has_Permisos.query.all()
    return jsonify([rol_has_permiso.to_dict() for rol_has_permiso in roles_has_permisos]), 200

@roles_has_permisos_bp.route('/roles_has_permisos/<int:roles_id>/<int:permisos_id>', methods=['GET'])
@jwt_required()
def get_rol_has_permiso(roles_id, permisos_id):
    rol_has_permiso = Roles_has_Permisos.query.get_or_404((roles_id, permisos_id))
    return jsonify(rol_has_permiso.to_dict()), 200

@roles_has_permisos_bp.route('/roles_has_permisos', methods=['POST'])
def create_rol_has_permiso():
    data = request.get_json()
    new_rol_has_permiso = Roles_has_Permisos(
        roles_id=data.get('roles_id'),
        permisos_id=data.get('permisos_id')
    )
    db.session.add(new_rol_has_permiso)
    db.session.commit()
    return jsonify(new_rol_has_permiso.to_dict()), 201

@roles_has_permisos_bp.route('/roles_has_permisos/<int:roles_id>/<int:permisos_id>', methods=['DELETE'])
def delete_rol_has_permiso(roles_id, permisos_id):
    rol_has_permiso = Roles_has_Permisos.query.get_or_404((roles_id, permisos_id))
    db.session.delete(rol_has_permiso)
    db.session.commit()
    return jsonify({'message': 'Rol_has_permiso eliminado'}), 200
