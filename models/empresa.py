from flask_sqlalchemy import SQLAlchemy
from extensions import db

class Empresa(db.Model):
    __tablename__ = 'empresa'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=True)  
    razon_social = db.Column(db.String(255), nullable=False)  
    direccion = db.Column(db.String(255), nullable=False)  
    telefono = db.Column(db.String(20), nullable=False)  
    logo = db.Column(db.String(255), nullable=True) 
    eslogan = db.Column(db.String(255), nullable=True)  
    tipo_empresa = db.Column(db.String(100), nullable=False)  
    nit = db.Column(db.Integer, nullable=True)  
    proyectos_id = db.Column(db.Integer, db.ForeignKey('proyectos.id'), nullable=True)
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)

    # Relaciones
    proyecto = db.relationship('Proyecto', back_populates='empresas')
    usuario = db.relationship('Usuario', back_populates='empresa')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'razon_social': self.razon_social,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'logo': self.logo,
            'eslogan': self.eslogan,
            'tipo_empresa': self.tipo_empresa,
            'nit': self.nit,
            'proyectos_id': self.proyectos_id,
            'usuarios_id': self.usuarios_id
        }
