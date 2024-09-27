from flask import Blueprint, request, jsonify
from models import db
from models.permisos import Permisos
import logging  # Asegúrate de importar logging
from flask_jwt_extended import jwt_required, get_jwt_identity



permisos_bp = Blueprint('permisos_bp', __name__)


@permisos_bp.route('/permisos', methods=['GET'])
# @jwt_required()
def get_permisos():
    try:
        permisos = Permisos.query.all()
        return jsonify({
            "message": "Permisos listados",
            "estado": 200,
            "data": [permiso.to_dict() for permiso in permisos]
        }), 200
    except Exception as e:
        # Registra el error para una mejor depuración
        print(f"Error al obtener permisos: {e}")
        return jsonify({"message": "Error al obtener permisos", "estado": 500}), 500

        
@permisos_bp.route('/permisos/<int:id>', methods=['GET'])
@jwt_required()
def get_permiso(id):
    permiso = Permisos.query.get_or_404(id)
    return jsonify(permiso.to_dict()), 200

@permisos_bp.route('/permisos', methods=['POST'])
def create_permiso():
    data = request.get_json()
    new_permiso = Permisos(
        id=data.get('id'),
        nombrePermiso=data.get('nombrePermiso')
    )
    db.session.add(new_permiso)
    db.session.commit()
    return jsonify(new_permiso.to_dict()), 201

@permisos_bp.route('/permisos/<int:id>', methods=['PUT'])
def update_permiso(id):
    permiso = Permisos.query.get_or_404(id)
    data = request.get_json()
    permiso.nombrePermiso = data.get('nombrePermiso', permiso.nombrePermiso)
    db.session.commit()
    return jsonify(permiso.to_dict()), 200

@permisos_bp.route('/permisos/<int:id>', methods=['DELETE'])
def delete_permiso(id):
    permiso = Permisos.query.get_or_404(id)
    db.session.delete(permiso)
    db.session.commit()
    return jsonify({'message': 'Permiso eliminado'}), 200
