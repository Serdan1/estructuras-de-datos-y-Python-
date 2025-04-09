from nodo.reina import Reina
from db.reina_movimiento import ReinaMovimiento
from db import Session
from datetime import datetime
import time

def es_seguro(tablero, fila, col, n):
    for j in range(col):
        if tablero[j] == fila:
            return False
    
    for i, j in zip(range(col-1, -1, -1), range(fila-1, -1, -1)):
        if tablero[i] == j:
            return False
    
    for i, j in zip(range(col-1, -1, -1), range(fila+1, n)):
        if tablero[i] == j:
            return False
    
    return True

def resolver_reinas(tablero, col, n):
    if col >= n:
        return True
    
    for fila in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[col] = fila
            if resolver_reinas(tablero, col + 1, n):
                return True
            tablero[col] = -1
    return False

def lanzar_reinas():
    n = int(input("Ingrese el tamaño del tablero (N, 1-15): "))
    if n < 1 or n > 15:
        print("Por favor, ingrese un valor de N entre 1 y 15.")
        return
    
    session = Session()
    # Buscar soluciones precalculadas para este N
    soluciones = session.query(ReinaMovimiento).filter_by(n=n).all()
    session.close()
    
    if not soluciones:
        print(f"No hay soluciones precalculadas para N={n}.")
        return
    
    # Tomar la primera solución (podríamos mostrar todas si quisiéramos)
    solucion = soluciones[0]
    tablero = list(map(int, solucion.solucion.split('-')))
    
    print(f"\nSolución encontrada para {n}-Reinas:")
    print("Vector (columna -> fila):", tablero)
    
    for fila in range(n):
        linea = ["Q" if tablero[col] == fila else "." for col in range(n)]
        print(" ".join(linea))