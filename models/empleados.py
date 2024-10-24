from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global
class Empleado(db.Model):
    __tablename__ = 'empleados'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    valor = db.Column(db.String(45), nullable=True)
    listado = db.Column(db.String(45), nullable=True)
    profesion = db.Column('Profesíon', db.String(45), nullable=True)  # Nombre de columna con tilde
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    # Define la relación con otras tablas
    facturacion = db.relationship("Facturacion", back_populates="empleados")
    estudios = db.relationship("Estudio", back_populates="empleados")
    experiencia = db.relationship("Experiencia", back_populates="empleados")

    def __repr__(self):
        return f"<Empleado(id={self.id}, valor={self.valor}, listado={self.listado}, profesion={self.profesion}, usuarios_id={self.usuarios_id})>"

    def to_dict(self):
        return {
            'id': self.id,
        'valor': self.valor,
        'listado': self.listado,
        'profesion': self.profesion,
        'usuarios_id': self.usuarios_id,
        'facturacion': [f.to_dict() for f in self.facturacion] if self.facturacion else None,
        'estudios': [e.to_dict() for e in self.estudios],
        'experiencia': [e.to_dict() for e in self.experiencia],
        }