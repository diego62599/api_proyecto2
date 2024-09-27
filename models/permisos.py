from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Permisos(db.Model):
    __tablename__ = 'permisos'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombrePermiso = db.Column(db.String(45), nullable=True)

    roles = db.relationship(
        'Roles',
        secondary='roles_has_permisos',
        back_populates='permisos'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'nombrePermiso': self.nombrePermiso
        }

    def __repr__(self):
        return f"<Permisos(id={self.id}, nombrePermiso={self.nombrePermiso})>"
