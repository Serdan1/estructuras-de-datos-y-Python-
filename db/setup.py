from . import Base, engine

def setup_database():
    # Importar las clases aquí para evitar dependencias circulares
    from .disco_movimiento import DiscoMovimiento
    from .caballo_movimiento import CaballoMovimiento
    from .reina_movimiento import ReinaMovimiento
    
    # Crear las tablas
    Base.metadata.create_all(engine)