from nodo.caballo import Caballo
from db.caballo_movimiento import CaballoMovimiento
from db import Session
from datetime import datetime
import time

def grado_salida(caballo, pos, visitado):
    caballo.posicion = pos
    return len([p for p in caballo.posibles_movimientos() if p not in visitado])

def resolver_caballo(caballo, tablero_visitado, secuencia):
    if len(secuencia) == 64:
        return True
    
    destinos = caballo.posibles_movimientos()
    destinos.sort(key=lambda pos: grado_salida(caballo, pos, tablero_visitado) if pos not in tablero_visitado else float('inf'))
    
    for destino in destinos:
        if destino not in tablero_visitado:
            tablero_visitado.add(destino)
            secuencia.append(destino)
            caballo.mover(destino)
            if resolver_caballo(caballo, tablero_visitado, secuencia):
                return True
            tablero_visitado.remove(destino)
            secuencia.pop()
            caballo.posicion = secuencia[-1] if secuencia else secuencia[0]
    return False

def lanzar_caballo():
    print("Solo están precalculados los recorridos para las posiciones (3,3) y (4,4).")
    x = int(input("Posición inicial X (0-7): "))
    y = int(input("Posición inicial Y (0-7): "))
    
    if not (0 <= x <= 7 and 0 <= y <= 7):
        print("Posición inválida. Debe estar entre 0 y 7.")
        return
    
    posicion_inicial = f"{x},{y}"
    if posicion_inicial not in ["3,3", "4,4"]:
        print(f"Lo siento, solo hay recorridos precalculados para las posiciones (3,3) y (4,4).")
        return
    
    session = Session()
    recorrido = session.query(CaballoMovimiento).filter_by(posicion_inicial=posicion_inicial).first()
    session.close()
    
    if not recorrido:
        print(f"No hay recorrido precalculado para la posición ({x},{y}).")
        return
    
    secuencia = [tuple(map(int, pos.split(','))) for pos in recorrido.secuencia.split('-')]
    
    print(f"\nRecorrido encontrado desde ({x},{y}):")
    print("Secuencia:", " -> ".join(f"{pos[0]},{pos[1]}" for pos in secuencia))
    print(f"Número de movimientos: {recorrido.pasos}")