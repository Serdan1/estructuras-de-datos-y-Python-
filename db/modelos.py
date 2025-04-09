from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ruta absoluta para Codespaces
engine = create_engine('sqlite:////workspaces/estructuras-de-datos-y-Python-/movimientos.db', echo=True)
Base = declarative_base()

class DiscoMovimiento(Base):
    __tablename__ = 'disco'
    id = Column(Integer, primary_key=True)
    n_discos = Column(Integer)         # Número total de discos
    movimiento = Column(String)        # Ej. "A->C"
    paso = Column(Integer)             # Orden del movimiento

# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)