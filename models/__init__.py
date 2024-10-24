from flask_sqlalchemy import SQLAlchemy


from extensions import db  # Usa la instancia global


from .empleados import Empleado

from .facturacion import Facturacion

from .proyecto import Proyecto

from .usuarios import Usuario

from .estudio import Estudio

from .experiencia import Experiencia

from .administracion import Administracion

from .listas_chequeo import ListasChequeo

from .permisos import Permisos

from .proyecto import Proyecto

from .proyectos_has_facturacion import ProyectosHasFacturacion

from .roles import Roles

from .roles_has_permisos import Roles_has_Permisos

from .roles_has_usuarios import Roles_has_Usuarios

from .usuarios import Usuario



from .listasChequeo_has_propiedades import ListasChequeoHasPropiedades


