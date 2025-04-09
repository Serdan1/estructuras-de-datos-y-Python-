from .nodo import Nodo

class Reina(Nodo):
    def __init__(self, posicion):
        super().__init__(posicion)

    def mover(self, destino):
        if self.validar_movimiento(destino):
            self.posicion = destino
            return f"Reina a {destino}"
        return None

    def validar_movimiento(self, destino):
        fila, col = destino
        return 0 <= fila < 8 and 0 <= col < 8