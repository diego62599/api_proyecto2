from flask import Blueprint, request, jsonify
from models import ListasChequeo ,ListasChequeoHasPropiedades
from models.listas_chequeo import ListasChequeo  
from models.propiedades import Propiedades 
from extensions import db  # Asegúrate de que db esté importado desde extensions
from flask_jwt_extended import jwt_required, get_jwt_identity




listas_chequeo_has_propiedades_bp = Blueprint('listas_chequeo_has_propiedades_bp', __name__)
@listas_chequeo_has_propiedades_bp.route('/listas_chequeo_has_propiedades', methods=['GET'])
# @jwt_required()
def get_listas_chequeo_has_propiedades():
    listas_chequeo_has_propiedades = ListasChequeoHasPropiedades.query.all()
    return jsonify([lc.to_dict() for lc in listas_chequeo_has_propiedades]), 200


@listas_chequeo_has_propiedades_bp.route('/listas_chequeo_has_propiedades/<int:listasChequeo_id>/<int:propiedades_id>', methods=['GET'])
@jwt_required()
def get_listas_chequeo_has_propiedad(listasChequeo_id, propiedades_id):
    listas_chequeo_has_propiedad = ListasChequeoHasPropiedades.query.filter_by(listasChequeo_id=listasChequeo_id, propiedades_id=propiedades_id).first()
    if listas_chequeo_has_propiedad:
        return jsonify(listas_chequeo_has_propiedad.serialize()), 200
    else:
        return jsonify({'message': 'Relación no encontrada'}), 404

@listas_chequeo_has_propiedades_bp.route('/listas_chequeo_has_propiedades', methods=['POST'])
def create_listas_chequeo_has_propiedad():
    try:
        data = request.get_json()
        listaschequeo_id = data.get('listasChequeo_id')
        propiedades_ids = data.get('propiedades_id')

        # Validar que el ID de listasChequeo exista
        lista_chequeo = ListasChequeo.query.get(listaschequeo_id)
        if not lista_chequeo:
            return jsonify({'message': 'ID de ListasChequeo no válido'}), 400

        # Validar que cada ID en propiedades_ids exista
        if not isinstance(propiedades_ids, list) or not propiedades_ids:
            return jsonify({'message': 'propiedades_id debe ser una lista válida'}), 400

        for prop_id in propiedades_ids:
            propiedad = Propiedades.query.get(prop_id)
            if not propiedad:
                return jsonify({'message': f'ID de Propiedad {prop_id} no válido'}), 400

            # Verificar si ya existe la relación
            existing_relation = ListasChequeoHasPropiedades.query.filter_by(
                listasChequeo_id=listaschequeo_id,
                propiedades_id=prop_id
            ).first()

            if existing_relation:
                return jsonify({'message': f'Relación ya existe para listasChequeo_id {listaschequeo_id} y propiedades_id {prop_id}'}), 400

            # Crear la relación para cada propiedad válida
            new_listas_chequeo_has_propiedad = ListasChequeoHasPropiedades(
                listasChequeo_id=listaschequeo_id,
                propiedades_id=prop_id
            )
            db.session.add(new_listas_chequeo_has_propiedad)

        db.session.commit()

        return jsonify({'message': 'Relaciones creadas con éxito'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al crear relación', 'error': str(e)}), 500


@listas_chequeo_has_propiedades_bp.route('/listas_chequeo_has_propiedades/<int:listasChequeo_id>/<int:propiedades_id>', methods=['PUT'])
def update_listas_chequeo_has_propiedad(listasChequeo_id, propiedades_id):
    listas_chequeo_has_propiedad = ListasChequeoHasPropiedades.query.filter_by(listasChequeo_id=listasChequeo_id, propiedades_id=propiedades_id).first()

    if not listas_chequeo_has_propiedad:
        return jsonify({'message': 'Relación no encontrada'}), 404

    data = request.json
    listasChequeo_id = data.get('listasChequeo_id')
    propiedades_id = data.get('propiedades_id')

    # Validar que los IDs existan en las tablas relacionadas
    if listasChequeo_id and not ListasChequeo.query.get(listasChequeo_id):
        return jsonify({'message': 'ID de ListasChequeo no válido'}), 400
    if propiedades_id and not Propiedades.query.get(propiedades_id):
        return jsonify({'message': 'ID de Propiedades no válido'}), 400

    listas_chequeo_has_propiedad.listasChequeo_id = listasChequeo_id or listas_chequeo_has_propiedad.listasChequeo_id
    listas_chequeo_has_propiedad.propiedades_id = propiedades_id or listas_chequeo_has_propiedad.propiedades_id

    db.session.commit()

    return jsonify(listas_chequeo_has_propiedad.serialize()), 200

@listas_chequeo_has_propiedades_bp.route('/listas_chequeo_has_propiedades/<int:listasChequeo_id>/<int:propiedades_id>', methods=['DELETE'])
def delete_listas_chequeo_has_propiedad(listasChequeo_id, propiedades_id):
    listas_chequeo_has_propiedad = ListasChequeoHasPropiedades.query.filter_by(listasChequeo_id=listasChequeo_id, propiedades_id=propiedades_id).first()

    if not listas_chequeo_has_propiedad:
        return jsonify({'message': 'Relación no encontrada'}), 404

    db.session.delete(listas_chequeo_has_propiedad)
    db.session.commit()

    return jsonify({'message': 'Relación eliminada correctamente'}), 200

