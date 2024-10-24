from flask import Blueprint, request, jsonify
from extensions import db
from models.empresa import Empresa
from flask_jwt_extended import jwt_required, get_jwt_identity

empresa_bp = Blueprint('empresa_bp', __name__)

# Obtener todas las empresas
@empresa_bp.route('/empresa', methods=['GET'])
# @jwt_required()  # Descomentar si se requiere autenticación JWT
def get_empresas():
    try:
        empresas = Empresa.query.all()
        return jsonify([empresa.to_dict() for empresa in empresas]), 200
    except Exception as e:
        return jsonify({'message': 'Error al obtener empresas', 'error': str(e)}), 500

# Obtener una empresa por ID
@empresa_bp.route('/empresa/<int:id>', methods=['GET'])
# @jwt_required()
def get_empresa(id):
    try:
        empresa = Empresa.query.get(id)
        if not empresa:
            return jsonify({'message': 'Empresa no encontrada'}), 404
        return jsonify(empresa.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'Error al obtener empresa', 'error': str(e)}), 500

# Crear una nueva empresa
@empresa_bp.route('/empresa', methods=['POST'])
# @jwt_required()
def create_empresa():
    try:
        data = request.get_json()
        new_empresa = Empresa(
            nombre=data.get('nombre'),
            razon_social=data.get('razon_social'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono'),
            logo=data.get('logo'),
            eslogan=data.get('eslogan'),
            tipo_empresa=data.get('tipo_empresa'),
            nit=data.get('nit'),
            proyectos_id=data.get('proyectos_id'),
            usuarios_id=data.get('usuarios_id')
        )
        db.session.add(new_empresa)
        db.session.commit()
        return jsonify(new_empresa.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al crear empresa', 'error': str(e)}), 500

# Actualizar una empresa existente
@empresa_bp.route('/empresa/<int:id>', methods=['PUT'])
# @jwt_required()
def update_empresa(id):
    try:
        data = request.get_json()
        empresa = Empresa.query.get(id)
        if not empresa:
            return jsonify({'message': 'Empresa no encontrada'}), 404
        empresa.nombre = data.get('nombre', empresa.nombre)
        empresa.razon_social = data.get('razon_social', empresa.razon_social)
        empresa.direccion = data.get('direccion', empresa.direccion)
        empresa.telefono = data.get('telefono', empresa.telefono)
        empresa.logo = data.get('logo', empresa.logo)
        empresa.eslogan = data.get('eslogan', empresa.eslogan)
        empresa.tipo_empresa = data.get('tipo_empresa', empresa.tipo_empresa)
        empresa.nit = data.get('nit', empresa.nit)
        empresa.proyectos_id = data.get('proyectos_id', empresa.proyectos_id)
        empresa.usuarios_id = data.get('usuarios_id', empresa.usuarios_id)
        db.session.commit()
        return jsonify(empresa.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al actualizar empresa', 'error': str(e)}), 500

# Eliminar una empresa
@empresa_bp.route('/empresa/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_empresa(id):
    try:
        empresa = Empresa.query.get(id)
        if not empresa:
            return jsonify({'message': 'Empresa no encontrada'}), 404
        db.session.delete(empresa)
        db.session.commit()
        return jsonify({'message': 'Empresa eliminada'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al eliminar empresa', 'error': str(e)}), 500
