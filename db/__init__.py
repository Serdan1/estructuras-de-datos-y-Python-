from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
engine = create_engine('sqlite:////workspaces/estructuras-de-datos-y-Python-/movimientos.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)