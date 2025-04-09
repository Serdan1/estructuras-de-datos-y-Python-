from nodo.disco import Disco
from db.disco_movimiento import DiscoMovimiento
from db import Session
from datetime import datetime

def resolver_hanoi(n, origen, auxiliar, destino, torres, movimientos, paso):
    if n == 1:
        disco = torres[origen][-1]
        mov = disco.mover(destino, torres)
        movimientos.append((mov, paso[0]))
        paso[0] += 1
        return
    
    resolver_hanoi(n-1, origen, destino, auxiliar, torres, movimientos, paso)
    disco = torres[origen][-1]
    mov = disco.mover(destino, torres)
    movimientos.append((mov, paso[0]))
    paso[0] += 1
    resolver_hanoi(n-1, auxiliar, origen, destino, torres, movimientos, paso)

def lanzar_hanoi(n=None, print_output=True):
    if n is None:
        n = int(input("Número de discos (1-10): "))
    
    if not (1 <= n <= 10):
        print("Por favor, ingrese un número de discos entre 1 y 10.")
        return "", ""
    
    session = Session()
    # Buscar movimientos precalculados para este n
    movimientos_db = session.query(DiscoMovimiento).filter_by(n_discos=n).order_by(DiscoMovimiento.paso).all()
    session.close()
    
    if not movimientos_db:
        print(f"No hay movimientos precalculados para n={n}.")
        return "", ""
    
    # Obtener el id_ejecucion más reciente
    id_ejecucion = max(mov.id_ejecucion for mov in movimientos_db)
    movimientos = [(mov.movimiento, mov.paso) for mov in movimientos_db if mov.id_ejecucion == id_ejecucion]
    
    # Simular el estado final de las torres usando objetos Disco
    torres = {
        'A': [Disco(i, 'A') for i in range(n, 0, -1)],
        'B': [],
        'C': []
    }
    for mov, _ in movimientos:
        # Parsear el movimiento (ej. "1: A -> C")
        tamano = int(mov.split(":")[0])
        origen, destino = mov.split(":")[1].split(" -> ")
        origen = origen.strip()
        destino = destino.strip()
        disco = next(d for d in torres[origen] if d.tamano == tamano)
        torres[origen].remove(disco)
        disco.posicion = destino
        torres[destino].append(disco)
    
    resultado = f"Movimientos ({len(movimientos)} totales):\n"
    resultado += "\n".join(f"{num_paso}. {mov}" for mov, num_paso in movimientos)
    
    visual = "Torres finales:\n"
    for torre, discos in torres.items():
        visual += f"{torre}: {[d.tamano for d in discos]}\n"
    
    if print_output:
        print(resultado)
        print(visual)
    
    return resultado, visual