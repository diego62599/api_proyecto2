from flask_sqlalchemy import SQLAlchemy
from extensions import db  # Usa la instancia global
from sqlalchemy.orm import relationship

class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombreProyecto = db.Column(db.String(45), nullable=True)
    tipoDeProyecto = db.Column(db.String(45), nullable=True)
    
    proyectos_has_facturacion = db.relationship('ProyectosHasFacturacion', back_populates='proyecto')
    empresas = db.relationship('Empresa', back_populates='proyecto')

    def to_dict(self):
        return {
            'id': self.id,
            'nombreProyecto': self.nombreProyecto,
            'tipoDeProyecto': self.tipoDeProyecto
        }
