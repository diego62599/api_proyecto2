from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global

class Propiedades(db.Model):
    __tablename__ = 'propiedades'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombrePropiedad = db.Column(db.String(45), nullable=True)
    tipo = db.Column(db.String(45), nullable=True)
    formato = db.Column(db.String(45), nullable=True)

    listas_chequeo_has_propiedades = db.relationship('ListasChequeoHasPropiedades', back_populates='propiedades')
    valor = db.relationship('Valor', back_populates='propiedades')


    def to_dict(self):
        return {
            'id': self.id,
            'nombrePropiedad': self.nombrePropiedad,
            'tipo': self.tipo,
            'formato': self.formato
        }


