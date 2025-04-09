from .nodo import Nodo

class Disco(Nodo):
    def __init__(self, tamano, posicion):
        super().__init__(posicion)
        self.tamano = tamano

    def mover(self, destino, torres):
        if self.validar_movimiento(destino, torres):
            torres[self.posicion].remove(self)
            self.posicion = destino
            torres[destino].append(self)
            return f"{self.tamano}: {self.posicion} -> {destino}"
        return None

    def validar_movimiento(self, destino, torres):
        if not torres[destino]:
            return True
        cima_destino = torres[destino][-1]
        return self.tamano < cima_destino.tamano