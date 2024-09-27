from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Roles_has_Usuarios(db.Model):
    __tablename__ = 'roles_has_usuarios'
    
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True, nullable=False)
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True, nullable=False)

    def to_dict(self):
        return {
            'roles_id': self.roles_id,
            'usuarios_id': self.usuarios_id
        }

