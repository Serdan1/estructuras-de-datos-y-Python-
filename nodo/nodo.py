from abc import ABC, abstractmethod

class Nodo(ABC):
    def __init__(self, posicion):
        self.posicion = posicion  # Torre donde está (A, B, C)

    @abstractmethod
    def mover(self, destino):
        pass

    @abstractmethod
    def validar_movimiento(self, destino):
        pass

class Disco(Nodo):
    def __init__(self, tamano, posicion):
        super().__init__(posicion)
        self.tamano = tamano  # Tamaño del disco (1 es el menor, N el mayor)

    def mover(self, destino, torres):
        if self.validar_movimiento(destino, torres):
            torres[self.posicion].remove(self)  # Quitar de la torre actual
            self.posicion = destino             # Actualizar posición
            torres[destino].append(self)        # Añadir a la torre destino
            return f"{self.tamano}: {self.posicion} -> {destino}"
        return None

    def validar_movimiento(self, destino, torres):
        # Si la torre destino está vacía, es válido
        if not torres[destino]:
            return True
        # El disco en la cima de destino debe ser mayor que este
        cima_destino = torres[destino][-1]
        return self.tamano < cima_destino.tamano