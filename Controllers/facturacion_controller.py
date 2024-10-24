from flask import Blueprint, request, jsonify, current_app
from models import db
from models.facturacion import Facturacion
from models.empleados import Empleado
from flask_jwt_extended import jwt_required, get_jwt_identity


facturacion_bp = Blueprint('facturacion_bp', __name__)

@facturacion_bp.route('/facturacion', methods=['POST'])

def create_facturacion():
    try:
        data = request.get_json()
        new_facturacion = Facturacion(
            id=data.get('id'),
            Fecha_factura=data.get('Fecha_factura'),
            Precio=data.get('Precio'),
            empleados_id=data.get('empleados_id')  # Añadido el campo empleados_id
        )
        db.session.add(new_facturacion)
        db.session.commit()
        current_app.logger.info(f'Facturación creada exitosamente con ID: {new_facturacion.id}')
        return jsonify({'message': 'Facturación creada exitosamente'}), 201
    except Exception as e:
        current_app.logger.error(f'Error al crear facturación: {str(e)}')
        return jsonify({'error': 'Error al crear facturación'}), 500

@facturacion_bp.route('/facturacion/<int:facturacion_id>', methods=['PUT'])
def update_facturacion(facturacion_id):
    try:
        data = request.get_json()
        facturacion = Facturacion.query.get_or_404(facturacion_id)
        
        if 'Fecha_factura' in data:
            facturacion.Fecha_factura = data['Fecha_factura']
        if 'Precio' in data:
            facturacion.Precio = data['Precio']
        if 'empleados_id' in data:
            facturacion.empleados_id = data['empleados_id']  # Actualiza el campo empleados_id
        
        db.session.commit()
        current_app.logger.info(f'Facturación actualizada exitosamente con ID: {facturacion.id}')
        return jsonify({'message': 'Facturación actualizada exitosamente'}), 200
    except Exception as e:
        current_app.logger.error(f'Error al actualizar facturación: {str(e)}')
        return jsonify({'error': 'Error al actualizar facturación'}), 500

@facturacion_bp.route('/facturacion/<int:facturacion_id>', methods=['DELETE'])
def delete_facturacion(facturacion_id):
    try:
        facturacion = Facturacion.query.get_or_404(facturacion_id)
        db.session.delete(facturacion)
        db.session.commit()
        current_app.logger.info(f'Facturación eliminada exitosamente con ID: {facturacion.id}')
        return jsonify({'message': 'Facturación eliminada exitosamente'}), 200
    except Exception as e:
        current_app.logger.error(f'Error al eliminar facturación: {str(e)}')
        return jsonify({'error': 'Error al eliminar facturación'}), 500

@facturacion_bp.route('/facturacion', methods=['GET'])
# @jwt_required()
def get_facturaciones():
    try:
        facturaciones = Facturacion.query.all()
        return jsonify([{
            'id': fac.id,
            'Fecha_factura': fac.Fecha_factura,
            'Precio': fac.Precio,
            'empleados_id': fac.empleados_id  
        } for fac in facturaciones]), 200
    except Exception as e:
        current_app.logger.error(f'Error al obtener facturaciones: {str(e)}')
        return jsonify({'error': 'Error al obtener facturaciones'}), 500
