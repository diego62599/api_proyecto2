from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global
class Valor(db.Model):
    __tablename__ = 'valor'
    
    idValor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Valor = db.Column(db.String(45), nullable=True)
    propiedades_id = db.Column(db.Integer, db.ForeignKey('propiedades.id'), nullable=False)
    listasChequeo_id = db.Column(db.Integer, db.ForeignKey('listaschequeo.id'), nullable=False)

    propiedades = db.relationship('Propiedades', back_populates='valor')
    lista_chequeo = db.relationship('ListasChequeo', back_populates='valor')

    def to_dict(self):
        return {
            'idValor': self.idValor,
            'Valor': self.Valor,
            'propiedades_id': self.propiedades_id,
            'listasChequeo_id': self.listasChequeo_id
        }

    def __repr__(self):
        return f"<Valor(idValor={self.idValor}, Valor={self.Valor}, propiedades_id={self.propiedades_id}, listasChequeo_id={self.listasChequeo_id})>"
        

   
