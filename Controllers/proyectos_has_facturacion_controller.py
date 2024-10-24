from flask import Blueprint, request, jsonify
from models.proyectos_has_facturacion import ProyectosHasFacturacion
from models.proyecto import Proyecto  
from models.facturacion import Facturacion 
from extensions import db  # Asegúrate de que db esté importado desde extensions
from flask_jwt_extended import jwt_required, get_jwt_identity


proyectos_has_facturacion_bp = Blueprint('proyectos_has_facturacion_bp', __name__)
@proyectos_has_facturacion_bp.route('/proyectos_has_facturacion', methods=['GET'])
@jwt_required()
def get_proyectos_has_facturacion():
    proyectos_has_facturacion = ProyectosHasFacturacion.query.all()
    return jsonify([pf.to_dict() for pf in proyectos_has_facturacion]), 200

@proyectos_has_facturacion_bp.route('/proyectos_has_facturacion/<int:proyectos_id>/<int:facturacion_id>', methods=['GET'])
@jwt_required()
def get_proyecto_has_facturacion(proyectos_id, facturacion_id):
    proyecto_has_facturacion = ProyectosHasFacturacion.query.filter_by(proyectos_id=proyectos_id, facturacion_id=facturacion_id).first()
    if proyecto_has_facturacion:
        return jsonify(proyecto_has_facturacion.serialize()), 200
    else:
        return jsonify({'message': 'Relación no encontrada'}), 404

@proyectos_has_facturacion_bp.route('/proyectos_has_facturacion', methods=['POST'])
def create_proyecto_has_facturacion():
    data = request.json
    proyectos_id = data.get('proyectos_id')
    facturacion_id = data.get('facturacion_id')

    # Validar que los IDs existan en las tablas relacionadas
    if not Proyecto.query.get(proyectos_id):
        return jsonify({'message': 'ID de Proyectos no válido'}), 400
    if not Facturacion.query.get(facturacion_id):
        return jsonify({'message': 'ID de Facturacion no válido'}), 400

    # Comprobar si la relación ya existe para evitar duplicados
    if ProyectosHasFacturacion.query.filter_by(proyectos_id=proyectos_id, facturacion_id=facturacion_id).first():
        return jsonify({'message': 'La relación ya existe'}), 400

    new_proyecto_has_facturacion = ProyectosHasFacturacion(proyectos_id=proyectos_id, facturacion_id=facturacion_id)
    db.session.add(new_proyecto_has_facturacion)
    db.session.commit()

    return jsonify(new_proyecto_has_facturacion.to_dict()), 201

@proyectos_has_facturacion_bp.route('/proyectos_has_facturacion/<int:proyectos_id>/<int:facturacion_id>', methods=['PUT'])
def update_proyecto_has_facturacion(proyectos_id, facturacion_id):
    proyecto_has_facturacion = ProyectosHasFacturacion.query.filter_by(proyectos_id=proyectos_id, facturacion_id=facturacion_id).first()

    if not proyecto_has_facturacion:
        return jsonify({'message': 'Relación no encontrada'}), 404

    data = request.json
    proyectos_id = data.get('proyectos_id')
    facturacion_id = data.get('facturacion_id')

    # Validar que los IDs existan en las tablas relacionadas
    if proyectos_id and not Proyectos.query.get(proyectos_id):
        return jsonify({'message': 'ID de Proyectos no válido'}), 400
    if facturacion_id and not Facturacion.query.get(facturacion_id):
        return jsonify({'message': 'ID de Facturacion no válido'}), 400

    proyecto_has_facturacion.proyectos_id = proyectos_id or proyecto_has_facturacion.proyectos_id
    proyecto_has_facturacion.facturacion_id = facturacion_id or proyecto_has_facturacion.facturacion_id

    db.session.commit()

    return jsonify(proyecto_has_facturacion.serialize()), 200

@proyectos_has_facturacion_bp.route('/proyectos_has_facturacion/<int:proyectos_id>/<int:facturacion_id>', methods=['DELETE'])
def delete_proyecto_has_facturacion(proyectos_id, facturacion_id):
    proyecto_has_facturacion = ProyectosHasFacturacion.query.filter_by(proyectos_id=proyectos_id, facturacion_id=facturacion_id).first()

    if not proyecto_has_facturacion:
        return jsonify({'message': 'Relación no encontrada'}), 404

    db.session.delete(proyecto_has_facturacion)
    db.session.commit()

    return jsonify({'message': 'Relación eliminada correctamente'}), 200
