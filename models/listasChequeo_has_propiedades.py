from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global

class ListasChequeoHasPropiedades(db.Model):
    __tablename__ = 'listasChequeo_has_propiedades'
    listasChequeo_id = db.Column(db.Integer, db.ForeignKey('listaschequeo.id'), primary_key=True)
    propiedades_id = db.Column(db.Integer, db.ForeignKey('propiedades.id'), primary_key=True)

    listaschequeo = db.relationship('ListasChequeo', back_populates='listas_chequeo_has_propiedades')
    propiedades = db.relationship('Propiedades', back_populates='listas_chequeo_has_propiedades')

    def to_dict(self):
        return {
            'listaschequeo_id': self.listasChequeo_id,
            'propiedades_id': self.propiedades_id
        }