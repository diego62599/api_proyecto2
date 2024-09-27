from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global

class Facturacion(db.Model):
    __tablename__ = 'facturacion'
    
    id = db.Column(db.Integer, primary_key=True)
    Fecha_factura = db.Column(db.String(45), nullable=True)
    Precio = db.Column(db.String(45), nullable=True)
    empleados_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)

    # Define la relación con Empleado
    empleados = db.relationship("Empleado", back_populates="facturacion")
    proyectos_has_facturacion = db.relationship('ProyectosHasFacturacion', back_populates='facturacion')

    def to_dict(self):
        return {
            'id': self.id,
            'Fecha_factura': self.Fecha_factura,
            'Precio': self.Precio
        }

    def __repr__(self):
        return f"<Facturacion(id={self.id}, Fecha_factura={self.Fecha_factura}, Precio={self.Precio})>"
