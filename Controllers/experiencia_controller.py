from flask import Blueprint, request, jsonify
from models import db
from models.experiencia import Experiencia
from flask_jwt_extended import jwt_required, get_jwt_identity


experiencia_bp = Blueprint('experiencia_bp', __name__)

# GET: Obtener todas las experiencias
@experiencia_bp.route('/experiencias', methods=['GET'])
# @jwt_required()
def get_experiencias():
    experiencias = Experiencia.query.all()
    return jsonify([experiencia.to_dict() for experiencia in experiencias]), 200



# GET: Obtener una experiencia por ID
@experiencia_bp.route('/experiencias/<int:id>', methods=['GET'])
# @jwt_required()
def get_experiencia(id):
    experiencia = Experiencia.query.get_or_404(id)
    return jsonify(experiencia.to_dict()), 200


# POST: Crear una nueva experiencia
@experiencia_bp.route('/experiencias', methods=['POST'])
def create_experiencia():
    data = request.get_json()
    new_experiencia = Experiencia(
        id=data.get('id'),
        Empresa=data.get('Empresa'),
        Fecha_inicio=data.get('Fecha_inicio'),
        Fecha_final=data.get('Fecha_final'),
        Cargo=data.get('Cargo'),
        Jefe_inmediato=data.get('Jefe_inmediato'),
        Documento=data.get('Documento'),
        empleados_id=data.get('empleados_id')
    )
    db.session.add(new_experiencia)
    db.session.commit()
    return jsonify(new_experiencia.to_dict()), 201

# PUT: Actualizar una experiencia existente
@experiencia_bp.route('/experiencias/<int:id>', methods=['PUT'])
def update_experiencia(id):
    experiencia = Experiencia.query.get_or_404((id))
    data = request.get_json()
    experiencia.Empresa = data.get('Empresa', experiencia.Empresa)
    experiencia.Fecha_inicio = data.get('Fecha_inicio', experiencia.Fecha_inicio)
    experiencia.Fecha_final = data.get('Fecha_final', experiencia.Fecha_final)
    experiencia.Cargo = data.get('Cargo', experiencia.Cargo)
    experiencia.Jefe_inmediato = data.get('Jefe_inmediato', experiencia.Jefe_inmediato)
    experiencia.Documento = data.get('Documento', experiencia.Documento)
    db.session.commit()
    return jsonify(experiencia.to_dict()), 200

# DELETE: Eliminar una experiencia
@experiencia_bp.route('/experiencias/<int:id>/<int:empleados_id>', methods=['DELETE'])
def delete_experiencia(id, empleados_id):
    experiencia = Experiencia.query.get_or_404((id, empleados_id))
    db.session.delete(experiencia)
    db.session.commit()
    return jsonify({'message': 'Experiencia eliminada'}), 200

