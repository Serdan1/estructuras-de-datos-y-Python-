from juegos.hanoi import lanzar_hanoi
from juegos.caballo import lanzar_caballo

def menu():
    while True:
        print("\n=== Menú de Juegos ===")
        print("1. Juego del Caballo")
        print("2. Juego de las N-Reinas")
        print("3. Juego de las Torres de Hanói")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            lanzar_caballo()
        elif opcion == '3':
            lanzar_hanoi()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no implementada aún.")

if __name__ == "__main__":
    menu()