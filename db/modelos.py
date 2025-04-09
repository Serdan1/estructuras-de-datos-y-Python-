from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////workspaces/estructuras-de-datos-y-Python-/movimientos.db', echo=True)
Base = declarative_base()

class DiscoMovimiento(Base):
    __tablename__ = 'disco'
    id = Column(Integer, primary_key=True)
    n_discos = Column(Integer)
    movimiento = Column(String)
    paso = Column(Integer)

class CaballoMovimiento(Base):
    __tablename__ = 'caballo'
    id = Column(Integer, primary_key=True)  # Corregido de 'Colloqueumn' a 'Column'
    posicion_inicial = Column(String)
    secuencia = Column(String)
    pasos = Column(Integer)

class ReinaMovimiento(Base):
    __tablename__ = 'reina'
    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    solucion = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)