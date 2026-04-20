from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# El archivo de la BD se creará en la raíz del proyecto
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Engine: El motor que conecta Python con SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal: Cada vez que alguien pida algo a la BD, le daremos una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: Clase de la que heredarán nuestros modelos de BD
Base = declarative_base()

# Función para obtener la DB en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
