from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db
from models.usuarios import Usuario
from models.roles import Roles
from models.roles_has_permisos import Roles_has_Permisos
from models.permisos import Permisos

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('Correo')
    contrasena = data.get('Contrasena')

    if not correo or not contrasena:
        return jsonify({'error': 'Correo y contraseña son requeridos'}), 400

    usuario = Usuario.query.filter_by(Correo=correo).first()

    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if usuario.Contrasena != contrasena:
        return jsonify({'error': 'Contraseña incorrecta'}), 401

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

    # Crear un JWT con todos los datos del usuario
    access_token = create_access_token(
        identity=usuario.id,  # Identificar al usuario por su ID
        additional_claims={
            'Nombre': usuario.Nombre,
            'Correo': usuario.Correo,
            'Documento': usuario.Documento,
            'tipoDocumento': usuario.tipoDocumento,
            'Apellido': usuario.Apellido,
            'Direccion': usuario.Direccion,
            'Telefono': usuario.Telefono,
            'Usuario': usuario.Usuario,
            'Sexo': usuario.Sexo,
            'Fotografia': usuario.Fotografia,
            'Rol': rol.to_dict() if rol else None,
            'Permisos': permisos_list
        }
    )

    return jsonify({
        'mensaje': 'Inicio de sesión exitoso',
        'access_token': access_token,
        'usuario': usuario.to_dict(),
        'roles': rol.to_dict() if rol else None,
        'permisos': permisos_list
    }), 200
