from nodo.nodo import Reina
from db.modelos import ReinaMovimiento, Session
import time

def es_seguro(tablero, fila, col, n):
    # Chequear fila a la izquierda
    for j in range(col):
        if tablero[j] == fila:
            return False
    
    # Chequear diagonal superior izquierda
    for i, j in zip(range(col-1, -1, -1), range(fila-1, -1, -1)):
        if tablero[i] == j:
            return False
    
    # Chequear diagonal inferior izquierda
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
            tablero[col] = -1  # Backtrack
    return False

def lanzar_reinas():
    n = int(input("Ingrese el tamaño del tablero (N, mínimo 4 recomendado): "))
    if n < 1:
        print("N debe ser mayor que 0.")
        return
    if n < 4 and n != 1:
        print("No hay soluciones para N < 4, excepto N = 1.")
        return
    
    # Inicializar tablero con -1 (sin reinas)
    tablero = [-1] * n
    inicio = time.time()
    
    if resolver_reinas(tablero, 0, n):
        fin = time.time()
        tiempo = fin - inicio
        
        # Guardar en la base de datos
        session = Session()
        solucion_str = "-".join(str(x) for x in tablero)
        registro = ReinaMovimiento(n=n, solucion=solucion_str)  # Pasar string directamente
        session.add(registro)
        session.commit()
        session.close()
        
        # Mostrar solución
        print(f"\nSolución encontrada para {n}-Reinas:")
        print("Vector (columna -> fila):", tablero)
        print(f"Tiempo: {tiempo:.2f} segundos")
        
        # Visualización simple del tablero
        for fila in range(n):
            linea = ["Q" if tablero[col] == fila else "." for col in range(n)]
            print(" ".join(linea))
    else:
        print("No se encontró solución (esto no debería pasar para N válido).")

if __name__ == "__main__":
    lanzar_reinas()