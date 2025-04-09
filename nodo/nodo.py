from abc import ABC, abstractmethod

class Nodo(ABC):
    def __init__(self, posicion):
        self.posicion = posicion

    @abstractmethod
    def mover(self, destino):
        pass

    @abstractmethod
    def validar_movimiento(self, destino):
        pass