from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global

class ListasChequeo(db.Model):
    __tablename__ = 'listaschequeo'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=True)

    listas_chequeo_has_propiedades = db.relationship('ListasChequeoHasPropiedades', back_populates='listaschequeo')
    valor = db.relationship('Valor', back_populates='lista_chequeo')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }

