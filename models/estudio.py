from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db  # Usa la instancia global

class Estudio(db.Model):
    __tablename__ = 'estudios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # Agrega autoincrement=True
    Institucion = db.Column('Institución', db.String(45), nullable=True)
    Graduado = db.Column(db.Boolean, nullable=True)
    Ano_de_grado = db.Column('Ano_de_grado', db.String(45), nullable=True)
    Titulo = db.Column(db.String(45), nullable=True)
    Documento = db.Column(db.String(45), nullable=True)
    empleados_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)

    empleados = db.relationship("Empleado", back_populates="estudios")

    def to_dict(self):
        return {
            'id': self.id,
            'Institucion': self.Institucion,
            'Graduado': self.Graduado,
            'Ano_de_grado': self.Ano_de_grado,
            'Titulo': self.Titulo,
            'Documento': self.Documento,
            'empleados_id': self.empleados_id
        }
