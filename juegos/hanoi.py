from nodo.nodo import Disco
from db.modelos import DiscoMovimiento, Session

def resolver_hanoi(n, origen, auxiliar, destino, torres, movimientos, paso):
    if n == 1:
        disco = torres[origen][-1]  # Tomar el disco de la cima
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

def lanzar_hanoi():
    n = int(input("Número de discos: "))
    
    torres = {
        'A': [Disco(i, 'A') for i in range(n, 0, -1)],
        'B': [],
        'C': []
    }
    
    movimientos = []
    paso = [1]
    
    resolver_hanoi(n, 'A', 'B', 'C', torres, movimientos, paso)
    
    session = Session()
    for mov, num_paso in movimientos:
        registro = DiscoMovimiento(n_discos=n, movimiento=mov, paso=num_paso)
        session.add(registro)
    session.commit()
    session.close()
    
    print(f"\nMovimientos ({len(movimientos)} totales):")
    for mov, num_paso in movimientos:
        print(f"{num_paso}. {mov}")

if __name__ == "__main__":
    lanzar_hanoi()