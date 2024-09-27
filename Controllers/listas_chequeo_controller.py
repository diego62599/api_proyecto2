from flask import Blueprint, request, jsonify
from models import db
from models.listas_chequeo import ListasChequeo
from flask_jwt_extended import jwt_required, get_jwt_identity


listas_chequeo_bp = Blueprint('listas_chequeo_bp', __name__)

@listas_chequeo_bp.route('/listas_chequeo', methods=['GET'])
@jwt_required()
def get_listas_chequeo():
    listas_chequeo = ListasChequeo.query.all()
    return jsonify([lista.to_dict() for lista in listas_chequeo]), 200

@listas_chequeo_bp.route('/listas_chequeo/<int:id>', methods=['GET'])
@jwt_required()
def get_lista_chequeo(id):
    lista_chequeo = ListasChequeo.query.get_or_404(id)
    return jsonify(lista_chequeo.to_dict()), 200

@listas_chequeo_bp.route('/listas_chequeo', methods=['POST'])
def create_lista_chequeo():
    data = request.get_json()
    new_lista_chequeo = ListasChequeo(
        id=data.get('id'),
        nombre=data.get('nombre')
    )
    db.session.add(new_lista_chequeo)
    db.session.commit()
    return jsonify(new_lista_chequeo.to_dict()), 201

@listas_chequeo_bp.route('/listas_chequeo/<int:id>', methods=['PUT'])
def update_lista_chequeo(id):
    lista_chequeo = ListasChequeo.query.get_or_404(id)
    data = request.get_json()
    lista_chequeo.nombre = data.get('nombre', lista_chequeo.nombre)
    db.session.commit()
    return jsonify(lista_chequeo.to_dict()), 200

@listas_chequeo_bp.route('/listas_chequeo/<int:id>', methods=['DELETE'])
def delete_lista_chequeo(id):
    lista_chequeo = ListasChequeo.query.get_or_404(id)
    db.session.delete(lista_chequeo)
    db.session.commit()
    return jsonify({'message': 'Lista de chequeo eliminada'}), 200
