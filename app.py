import logging
from flask import Flask, jsonify
# from flask_mail import Mail, Message
from config import DevelopmentConfig
from extensions import db 
import utils
from sqlalchemy import inspect  
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import boto3

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logging.debug('Este es un mensaje de debug')
logging.info('Este es un mensaje informativo')
logging.warning('Este es un mensaje de advertencia')
logging.error('Este es un mensaje de error')
logging.critical('Este es un mensaje crítico')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializar la base de datos
db.init_app(app)

app.config['JWT_SECRET_KEY'] = 'Goofy62599'  

jwt = JWTManager(app)
CORS(app)



s3_client = boto3.client('s3')




# Configuración de correo electrónico (comentar si no se usa)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'diegobetancur62599@gmail.com'
# app.config['MAIL_PASSWORD'] = 'lpqk htdg wkhm lsqb'

# mail = Mail(app)

# Importar y registrar los Blueprints
from Controllers.empleados_controller import empleados_bp
from Controllers.facturacion_controller import facturacion_bp
from Controllers.usuarios_controller import usuarios_bp
from Controllers.proyectos_controller import proyectos_bp
from Controllers.estudios_controller import estudios_bp
from Controllers.experiencia_controller import experiencia_bp
from Controllers.administracion_controller import administracion_bp
from Controllers.roles_controller import roles_bp
from Controllers.permisos_controller import permisos_bp
from Controllers.roles_has_permisos_controller import roles_has_permisos_bp
from Controllers.listas_chequeo_controller import listas_chequeo_bp
from Controllers.propiedades_controller import propiedades_bp
from Controllers.listasChequeo_has_propiedades_controller import listas_chequeo_has_propiedades_bp
from Controllers.roles_has_usuarios_controller import roles_has_usuarios_bp
from Controllers.empresa_controller import empresa_bp
from Controllers.proyectos_has_facturacion_controller import proyectos_has_facturacion_bp
from Controllers.valor_controller import valor_bp
from Controllers.login_controller import login_bp
from Controllers.protected_controller import protected_bp

app.register_blueprint(empleados_bp)
app.register_blueprint(facturacion_bp)
app.register_blueprint(proyectos_bp)
app.register_blueprint(estudios_bp)
app.register_blueprint(experiencia_bp)
app.register_blueprint(administracion_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(permisos_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(roles_has_permisos_bp)
app.register_blueprint(listas_chequeo_bp)
app.register_blueprint(propiedades_bp)
app.register_blueprint(listas_chequeo_has_propiedades_bp)
app.register_blueprint(roles_has_usuarios_bp)
app.register_blueprint(empresa_bp)
app.register_blueprint(proyectos_has_facturacion_bp)
app.register_blueprint(valor_bp)
app.register_blueprint(login_bp)
app.register_blueprint(protected_bp)




# Definir una función de manejo de errores
def handle_error(error):
    response = {
        "message": str(error),
        "status": 500
    }
    return jsonify(response), 500

@app.errorhandler(Exception)
def handle_all_exceptions(error):
    return handle_error(error)

# Verificar la conexión a la base de datos al iniciar la API
if __name__ == '__main__':
    # with app.app_context():
    #     try:
    #         # Verificar si se pueden obtener las tablas, lo que indica una conexión exitosa
    #         inspector = inspect(db.engine)
    #         tables = inspector.get_table_names()
    #         if tables:
    #             logging.info(f"Conexión a la base de datos exitosa. Tablas: {tables}")
    #         else:
    #             logging.warning("No se encontraron tablas en la base de datos.")
    #     except Exception as e:
    #         logging.error(f"Error al conectar a la base de datos: {str(e)}")

    # Iniciar la aplicación
    app.run(debug=True)