from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Experiencia(db.Model):
    __tablename__ = 'experiencia'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # Agrega autoincrement=True
    Empresa = db.Column(db.String(45), nullable=True)
    Fecha_inicio = db.Column(db.String(45), nullable=True)
    Fecha_final = db.Column(db.String(45), nullable=True)
    Cargo = db.Column(db.String(45), nullable=True)
    Jefe_inmediato = db.Column(db.String(45), nullable=True)
    Documento = db.Column(db.String(45), nullable=True)
    empleados_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)


    empleados = db.relationship("Empleado", back_populates="experiencia")

    def to_dict(self):
        return {
            'id': self.id,
            'Empresa': self.Empresa,
            'Fecha_inicio': self.Fecha_inicio,
            'Fecha_final': self.Fecha_final,
            'Cargo': self.Cargo,
            'Jefe_inmediato': self.Jefe_inmediato,
            'Documento': self.Documento,
            'empleados_id': self.empleados_id
        }
