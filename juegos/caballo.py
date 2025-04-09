from nodo.nodo import Caballo
from db.modelos import CaballoMovimiento, Session

def explorar_caballo(caballo, pasos_restantes, secuencia, movimientos):
    if pasos_restantes == 0:
        # Guardar la secuencia completa
        movimientos.append(secuencia[:])
        return
    
    # Obtener posibles movimientos desde la posición actual
    destinos = caballo.posibles_movimientos()
    for destino in destinos:
        # Mover el caballo y añadir la nueva posición a la secuencia
        caballo.mover(destino)
        secuencia.append(destino)
        explorar_caballo(caballo, pasos_restantes - 1, secuencia, movimientos)
        # Retroceder (backtracking)
        secuencia.pop()
        caballo.posicion = secuencia[-1] if secuencia else caballo.posicion

def lanzar_caballo():
    # Pedir posición inicial y número de pasos
    x = int(input("Posición inicial X (0-7): "))
    y = int(input("Posición inicial Y (0-7): "))
    pasos = int(input("Número de pasos: "))
    
    # Validar entrada
    if not (0 <= x <= 7 and 0 <= y <= 7):
        print("Posición inválida. Debe estar entre 0 y 7.")
        return
    
    # Inicializar el caballo
    caballo = Caballo((x, y))
    movimientos = []
    secuencia = [(x, y)]  # Iniciar con la posición inicial
    
    # Explorar todos los caminos
    explorar_caballo(caballo, pasos, secuencia, movimientos)
    
    # Guardar en la base de datos
    session = Session()
    for mov in movimientos:
        secuencia_str = "-".join(f"{pos[0]},{pos[1]}" for pos in mov)
        registro = CaballoMovimiento(
            posicion_inicial=f"{x},{y}",
            secuencia=secuencia_str,
            pasos=pasos
        )
        session.add(registro)
    session.commit()
    session.close()
    
    # Mostrar resultados
    print(f"\nSecuencias válidas para {pasos} pasos desde ({x},{y}):")
    for i, mov in enumerate(movimientos, 1):
        secuencia_str = " -> ".join(f"{pos[0]},{pos[1]}" for pos in mov)
        print(f"{i}. {secuencia_str}")

if __name__ == "__main__":
    lanzar_caballo()