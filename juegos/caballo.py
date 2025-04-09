from nodo.caballo import Caballo
from db.modelos import CaballoMovimiento, Session
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
    print("Recomendamos empezar en la posición X=3, Y=3 para un cálculo rápido.")
    x = int(input("Posición inicial X (0-7): "))
    y = int(input("Posición inicial Y (0-7): "))
    
    if not (0 <= x <= 7 and 0 <= y <= 7):
        print("Posición inválida. Debe estar entre 0 y 7.")
        return
    
    caballo = Caballo((x, y))
    tablero_visitado = {(x, y)}
    secuencia = [(x, y)]
    
    inicio = time.time()
    exito = resolver_caballo(caballo, tablero_visitado, secuencia)
    fin = time.time()
    tiempo = fin - inicio
    
    if exito:
        session = Session()
        secuencia_str = "-".join(f"{pos[0]},{pos[1]}" for pos in secuencia)
        registro = CaballoMovimiento(
            posicion_inicial=f"{x},{y}",
            secuencia=secuencia_str,
            pasos=len(secuencia) - 1
        )
        session.add(registro)
        session.commit()
        session.close()
        
        print(f"\nRecorrido encontrado desde ({x},{y}):")
        print("Secuencia:", " -> ".join(f"{pos[0]},{pos[1]}" for pos in secuencia))
        print(f"Número de movimientos: {len(secuencia) - 1}")
        print(f"Tiempo: {tiempo:.2f} segundos")
    else:
        print("No se encontró un recorrido completo desde esa posición.")
        print(f"Tiempo: {tiempo:.2f} segundos")