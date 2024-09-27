from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.usuarios import Usuario
from models.roles import Roles
from models.roles_has_permisos import Roles_has_Permisos
from models.permisos import Permisos

protected_bp = Blueprint('protected_bp', __name__)

@protected_bp.route('/protected', methods=['GET'])
@jwt_required()
def profile():
    # Obtener la identidad del JWT
    user_id = get_jwt_identity()

    # Buscar al usuario por ID
    usuario = Usuario.query.get(user_id)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Obtener el rol asociado al usuario
    rol = Roles.query.get(usuario.roles_id)

    # Obtener los permisos asociados al rol
    permisos = (
        db.session.query(Permisos)
        .join(Roles_has_Permisos, Permisos.id == Roles_has_Permisos.permisos_id)
        .filter(Roles_has_Permisos.roles_id == rol.id)
        .all()
    )

    permisos_list = [permiso.to_dict() for permiso in permisos]

    return jsonify({
        'user': usuario.to_dict(),
        'role': rol.to_dict() if rol else None,
        'permissions': permisos_list
    }), 200
