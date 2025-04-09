from sqlalchemy import Column, Integer, String, DateTime
from . import Base
from datetime import datetime, timezone

class ReinaMovimiento(Base):
    __tablename__ = 'reina'
    id = Column(Integer, primary_key=True)
    id_ejecucion = Column(Integer)
    n = Column(Integer)
    solucion = Column(String)
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))