from flask import Blueprint, request, jsonify
from extensions import db
from models.valor import Valor
from models.listas_chequeo import ListasChequeo
from models.propiedades import Propiedades
from flask_jwt_extended import jwt_required, get_jwt_identity


valor_bp = Blueprint('valor_bp', __name__)

@valor_bp.route('/valor', methods=['GET'])
def get_valores():
    try:
        valores = Valor.query.all()
        return jsonify([valor.to_dict() for valor in valores]), 200
    except Exception as e:
        return jsonify({'error': f'Error al obtener valores: {str(e)}'}), 500

@valor_bp.route('/valor/<int:idValor>', methods=['GET'])
def get_valor(idValor):
    try:
        valor = Valor.query.get_or_404(idValor)
        return jsonify(valor.to_dict()), 200
    except Exception as e:
        return jsonify({'error': f'Valor no encontrado: {str(e)}'}), 404

@valor_bp.route('/valor', methods=['POST'])
def create_valor():
    try:
        data = request.get_json()
        new_valor = Valor(
            Valor=data.get('Valor'),
            propiedades_id=data.get('propiedades_id'),
            listasChequeo_id=data.get('listasChequeo_id')
        )
        db.session.add(new_valor)
        db.session.commit()
        return jsonify(new_valor.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al crear valor: {str(e)}'}), 500

@valor_bp.route('/valor/<int:idValor>', methods=['PUT'])
def update_valor(idValor):
    try:
        data = request.get_json()
        valor = Valor.query.get_or_404(idValor)
        valor.Valor = data.get('Valor', valor.Valor)
        valor.propiedades_id = data.get('propiedades_id', valor.propiedades_id)
        valor.listasChequeo_id = data.get('listasChequeo_id', valor.listasChequeo_id)
        db.session.commit()
        return jsonify(valor.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al actualizar valor: {str(e)}'}), 500

@valor_bp.route('/valor/<int:idValor>', methods=['DELETE'])
def delete_valor(idValor):
    try:
        valor = Valor.query.get_or_404(idValor)
        db.session.delete(valor)
        db.session.commit()
        return jsonify({'message': 'Valor eliminado'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al eliminar valor: {str(e)}'}), 500