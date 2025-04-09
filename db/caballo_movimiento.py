from sqlalchemy import Column, Integer, String, DateTime
from . import Base
from datetime import datetime, timezone

class CaballoMovimiento(Base):
    __tablename__ = 'caballo'
    id = Column(Integer, primary_key=True)
    id_ejecucion = Column(Integer)
    posicion_inicial = Column(String)
    secuencia = Column(String)
    pasos = Column(Integer)
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))