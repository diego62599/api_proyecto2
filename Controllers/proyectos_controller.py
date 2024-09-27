from flask import Blueprint, request, jsonify
from models import db
from models.proyecto import Proyecto
from flask_jwt_extended import jwt_required, get_jwt_identity


proyectos_bp = Blueprint('proyectos_bp', __name__)


@proyectos_bp.route('/proyectos', methods=['GET'])
# @jwt_required()
def get_proyectos():
    proyectos = Proyecto.query.all()
    return jsonify([proyecto.to_dict() for proyecto in proyectos]), 200


@proyectos_bp.route('/proyectos/<int:id>', methods=['GET'])
@jwt_required()
def get_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    return jsonify(proyecto.to_dict()), 200


@proyectos_bp.route('/proyectos', methods=['POST'])
def create_proyecto():
    data = request.get_json()
    new_proyecto = Proyecto(
        id=data.get('id'),
        nombreProyecto=data.get('nombreProyecto'),
        tipoDeProyecto=data.get('tipoDeProyecto')
    )
    db.session.add(new_proyecto)
    db.session.commit()
    return jsonify(new_proyecto.to_dict()), 201


@proyectos_bp.route('/proyectos/<int:id>', methods=['PUT'])
def update_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    data = request.get_json()
    proyecto.nombreProyecto = data.get('nombreProyecto', proyecto.nombreProyecto)
    proyecto.tipoDeProyecto = data.get('tipoDeProyecto', proyecto.tipoDeProyecto)
    db.session.commit()
    return jsonify(proyecto.to_dict()), 200


@proyectos_bp.route('/proyectos/<int:id>', methods=['DELETE'])
def delete_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    db.session.delete(proyecto)
    db.session.commit()
    return jsonify({'message': 'Proyecto eliminado'}), 200
