from flask import Blueprint, request, jsonify, current_app
from models import db
from models.empleados import Empleado
from models.facturacion import Facturacion
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS


empleados_bp = Blueprint('empleados_bp', __name__)

@empleados_bp.route('/empleados', methods=['GET'])
# @jwt_required()
def get_empleados():
    try:
        empleados = Empleado.query.all()
        empleados_list = [{
            'id': emp.id,
            'valor': emp.valor,
            'listado': emp.listado,
            'profesion': emp.profesion,
            'usuarios_id': emp.usuarios_id,
        } for emp in empleados]
        
        db.session.close()

        return jsonify({'empleados': empleados_list, 'mensaje': 'Empleados listados'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al obtener empleados: {str(e)}'}), 500

@empleados_bp.route('/empleado/<int:id>', methods=['GET'])
# @jwt_required()
def get_empleado(id):
    empleado = Empleado.query.get(id)
    
    if not empleado:
        return jsonify({'message': 'Empleado no encontrado'}), 404
    
    return jsonify(empleado.to_dict()), 200

@empleados_bp.route('/empleados', methods=['POST'])
def create_empleado():
        try:
            data = request.get_json()
            new_empleado = Empleado(
                valor=data.get('valor'),
                listado=data.get('listado'),
                profesion=data.get('profesion'),
                usuarios_id=data.get('usuarios_id')
            )
            db.session.add(new_empleado)
            db.session.commit()
            return jsonify(new_empleado.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error al crear empleado', 'mensaje': str(e)}), 500

@empleados_bp.route('/empleados/<int:id>', methods=['PUT'])
def update_empleado(id):
    try:
        empleado = Empleado.query.get_or_404(id)
        data = request.get_json()
        empleado.valor = data.get('valor', empleado.valor)
        empleado.listado = data.get('listado', empleado.listado)
        empleado.profesion = data.get('profesion', empleado.profesion)
        empleado.usuarios_id = data.get('usuarios_id', empleado.usuarios_id)

        db.session.commit()
        return jsonify(empleado.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al actualizar empleado', 'mensaje': str(e)}), 500

@empleados_bp.route('/empleados/<int:id>', methods=['DELETE'])
def delete_empleado(id):
    try:
        empleado = Empleado.query.get_or_404(id)
        db.session.delete(empleado)
        db.session.commit()
        return jsonify({'mensaje': 'Empleado eliminado'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error al eliminar empleado', 'mensaje': str(e)}), 500
