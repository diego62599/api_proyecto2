from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Roles_has_Permisos(db.Model):
    __tablename__ = 'roles_has_permisos'
    
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True, nullable=False)
    permisos_id = db.Column(db.Integer, db.ForeignKey('permisos.id'), primary_key=True, nullable=False)

    # permisos = db.relationship('Permisos', backref='roles_has_permisos')

    def to_dict(self):
        return {
            'roles_id': self.roles_id,
            'permisos_id': self.permisos_id
        }
