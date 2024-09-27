from flask import Blueprint, request, jsonify
from models import db
from models.estudio import Estudio
from flask_jwt_extended import jwt_required, get_jwt_identity


estudios_bp = Blueprint('estudios_bp', __name__)


@estudios_bp.route('/estudios', methods=['GET'])
# @jwt_required()
def get_estudios():
    estudios = Estudio.query.all()
    return jsonify([estudio.to_dict() for estudio in estudios]), 200


@estudios_bp.route('/estudios/<int:id>/<int:empleados_id>', methods=['GET'])
@jwt_required()
def get_estudio(id, empleados_id):
    estudio = Estudio.query.get_or_404((id, empleados_id))
    return jsonify(estudio.to_dict()), 200


    
@estudios_bp.route('/estudios', methods=['POST'])
def create_estudio():
    try:
        data = request.get_json()
        new_estudio = Estudio(
            id=data.get('id'),
            Institucion=data.get('Institucion'),  
            Graduado=data.get('Graduado'),        
            Ano_de_grado=data.get('Ano_de_grado'), 
            Titulo=data.get('Titulo'),      
            Documento=data.get('Documento'),      
            empleados_id=data.get('empleados_id')
        )
        db.session.add(new_estudio)
        db.session.commit()
        return jsonify(new_estudio.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al crear estudio', 'mensaje': str(e)}), 500

@estudios_bp.route('/estudios/<int:id>', methods=['PUT'])
def update_estudio(id):
    estudio = Estudio.query.get_or_404(id)
    data = request.get_json()
    # Usa 'get' para asignar el valor solo si está presente en el JSON
    estudio.Institucion = data.get('Institucion', estudio.Institucion)
    estudio.Graduado = data.get('Graduado', estudio.Graduado)
    estudio.Ano_de_grado = data.get('Ano_de_grado', estudio.Ano_de_grado)
    estudio.Titulo = data.get('Titulo', estudio.Titulo)
    estudio.Documento = data.get('Documento', estudio.Documento)
    db.session.commit()
    return jsonify(estudio.to_dict()), 200


@estudios_bp.route('/estudios/<int:id>/<int:empleados_id>', methods=['DELETE'])
def delete_estudio(id, empleados_id):
    estudio = Estudio.query.get_or_404((id, empleados_id))
    db.session.delete(estudio)
    db.session.commit()
    return jsonify({'message': 'Estudio eliminado'}), 200
