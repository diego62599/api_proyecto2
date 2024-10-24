class DevelopmentConfig:
    DEBUG = True
    # Configuración para la base de datos remota
    DB_HOST = 'ebulky.cbf50kwzyuxm.us-east-1.rds.amazonaws.com'
    DB_PORT = 3306
    DB_NAME = 'eb_source'
    DB_USERNAME = 'Ebulkyadmin'
    DB_PASSWORD = 'Ebulkyadmin*#'
    
    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False