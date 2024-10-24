from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from extensions import db  # Usa la instancia global

class Roles(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(45), nullable=True)
    estado = db.Column(db.Boolean, nullable=True)

      
    permisos = db.relationship(
        'Permisos',
        secondary='roles_has_permisos',
        back_populates='roles'
    )
    
    usuarios = db.relationship(
        'Usuario',
        back_populates='roles'
    )



    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'estado': self.estado
        }

    def __repr__(self):
        return f"<Roles(id={self.id}, nombre={self.nombre})>"
