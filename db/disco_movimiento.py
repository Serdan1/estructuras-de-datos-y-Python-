from sqlalchemy import Column, Integer, String, DateTime
from . import Base
from datetime import datetime, timezone

class DiscoMovimiento(Base):
    __tablename__ = 'disco'
    id = Column(Integer, primary_key=True)
    id_ejecucion = Column(Integer)
    n_discos = Column(Integer)
    movimiento = Column(String)
    paso = Column(Integer)
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))