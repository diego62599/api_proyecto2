from flask import Blueprint, request, jsonify
from models import db
from models.administracion import Administracion
from flask_jwt_extended import jwt_required, get_jwt_identity


administracion_bp = Blueprint('administracion_bp', __name__)


@administracion_bp.route('/administraciones', methods=['GET'])
# @jwt_required()
def get_administraciones():
    administraciones = Administracion.query.all()
    return jsonify([administracion.to_dict() for administracion in administraciones]), 200


@administracion_bp.route('/administraciones/<int:id>/<int:usuarios_id>', methods=['GET'])
# @jwt_required()
def get_administracion(id, usuarios_id):
    administracion = Administracion.query.get_or_404((id, usuarios_id))
    return jsonify(administracion.to_dict()), 200


@administracion_bp.route('/administraciones', methods=['POST'])
def create_administracion():
    data = request.get_json()
    new_administracion = Administracion(
        id=data.get('id'),
        cargo=data.get('cargo'),
        dependencia=data.get('dependencia'),
        usuarios_id=data.get('usuarios_id')
    )
    db.session.add(new_administracion)
    db.session.commit()
    return jsonify(new_administracion.to_dict()), 201


@administracion_bp.route('/administraciones/<int:id>', methods=['PUT'])
def update_administracion(id):
    administracion = Administracion.query.get_or_404((id))
    data = request.get_json()
    administracion.cargo = data.get('cargo', administracion.cargo)
    administracion.dependencia = data.get('dependencia', administracion.dependencia)
    db.session.commit()
    return jsonify(administracion.to_dict()), 200


@administracion_bp.route('/administraciones/<int:id>/<int:usuarios_id>', methods=['DELETE'])
def delete_administracion(id, usuarios_id):
    administracion = Administracion.query.get_or_404((id, usuarios_id))
    db.session.delete(administracion)
    db.session.commit()
    return jsonify({'message': 'Administracion eliminada'}), 200
