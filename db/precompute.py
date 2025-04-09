from db import Session
from db.disco_movimiento import DiscoMovimiento
from db.caballo_movimiento import CaballoMovimiento
from db.reina_movimiento import ReinaMovimiento
from datetime import datetime

# Para Hanói
from juegos.hanoi import resolver_hanoi
from nodo.disco import Disco

# Para Caballo
from juegos.caballo import resolver_caballo, grado_salida
from nodo.caballo import Caballo

# Para N-Reinas
from juegos.reinas import resolver_reinas, es_seguro

def precompute_hanoi():
    session = Session()
    
    # Precalcular para n de 1 a 10
    for n in range(1, 11):
        # Verificar si ya existen movimientos para este n
        if session.query(DiscoMovimiento).filter_by(n_discos=n).count() > 0:
            print(f"Movimientos para Hanói con n={n} ya precalculados.")
            continue
        
        print(f"Precalculando Hanói para n={n}...")
        torres = {
            'A': [Disco(i, 'A') for i in range(n, 0, -1)],
            'B': [],
            'C': []
        }
        movimientos = []
        paso = [1]
        id_ejecucion = int(datetime.now().timestamp() * 1000)
        
        resolver_hanoi(n, 'A', 'B', 'C', torres, movimientos, paso)
        
        for mov, num_paso in movimientos:
            registro = DiscoMovimiento(
                id_ejecucion=id_ejecucion,
                n_discos=n,
                movimiento=mov,
                paso=num_paso
            )
            session.add(registro)
    
    session.commit()
    session.close()

def precompute_caballo():
    session = Session()
    
    # Precalcular para cada posición inicial (0,0) a (7,7)
    for x in range(8):
        for y in range(8):
            posicion_inicial = f"{x},{y}"
            # Verificar si ya existe un recorrido para esta posición
            if session.query(CaballoMovimiento).filter_by(posicion_inicial=posicion_inicial).count() > 0:
                print(f"Recorrido para Caballo desde ({x},{y}) ya precalculado.")
                continue
            
            print(f"Precalculando Caballo para posición inicial ({x},{y})...")
            caballo = Caballo((x, y))
            tablero_visitado = {(x, y)}
            secuencia = [(x, y)]
            id_ejecucion = int(datetime.now().timestamp() * 1000)
            
            exito = resolver_caballo(caballo, tablero_visitado, secuencia)
            
            if exito:
                secuencia_str = "-".join(f"{pos[0]},{pos[1]}" for pos in secuencia)
                registro = CaballoMovimiento(
                    id_ejecucion=id_ejecucion,
                    posicion_inicial=posicion_inicial,
                    secuencia=secuencia_str,
                    pasos=len(secuencia) - 1
                )
                session.add(registro)
    
    session.commit()
    session.close()

def precompute_reinas():
    session = Session()
    
    # Precalcular para N de 1 a 15
    for n in range(1, 16):
        # Verificar si ya existen soluciones para este N
        if session.query(ReinaMovimiento).filter_by(n=n).count() > 0:
            print(f"Soluciones para N-Reinas con N={n} ya precalculadas.")
            continue
        
        print(f"Precalculando N-Reinas para N={n}...")
        soluciones = []
        tablero = [-1] * n
        
        def backtrack(col):
            if col >= n:
                soluciones.append(tablero[:])
                return
            for fila in range(n):
                if es_seguro(tablero, fila, col, n):
                    tablero[col] = fila
                    backtrack(col + 1)
                    tablero[col] = -1
        
        backtrack(0)
        
        id_ejecucion = int(datetime.now().timestamp() * 1000)
        for solucion in soluciones:
            solucion_str = "-".join(str(x) for x in solucion)
            registro = ReinaMovimiento(
                id_ejecucion=id_ejecucion,
                n=n,
                solucion=solucion_str
            )
            session.add(registro)
    
    session.commit()
    session.close()

def precompute_all():
    print("Precalculando datos para todos los juegos...")
    precompute_hanoi()
    precompute_caballo()
    precompute_reinas()
    print("Precomputo completado.")