from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global

class ProyectosHasFacturacion(db.Model):
    __tablename__ = 'proyectos_has_facturacion'
    
    proyectos_id = db.Column(db.Integer, db.ForeignKey('proyectos.id'), primary_key=True, nullable=False)
    facturacion_id = db.Column(db.Integer, db.ForeignKey('facturacion.id'), primary_key=True, nullable=False)

    proyecto = db.relationship("Proyecto", back_populates="proyectos_has_facturacion")
    facturacion = db.relationship("Facturacion", back_populates="proyectos_has_facturacion")

    def to_dict(self):
        return {
            'proyectos_id': self.proyectos_id,
            'facturacion_id': self.facturacion_id,
        }
