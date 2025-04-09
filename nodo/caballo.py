from .nodo import Nodo

class Caballo(Nodo):
    def __init__(self, posicion):
        super().__init__(posicion)

    def mover(self, destino):
        if self.validar_movimiento(destino):
            self.posicion = destino
            return f"{self.posicion[0]},{self.posicion[1]} -> {destino[0]},{destino[1]}"
        return None

    def validar_movimiento(self, destino):
        if not (0 <= destino[0] <= 7 and 0 <= destino[1] <= 7):
            return False
        dx = abs(destino[0] - self.posicion[0])
        dy = abs(destino[1] - self.posicion[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    def posibles_movimientos(self):
        movimientos = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        actuales = []
        for dx, dy in movimientos:
            nueva_x = self.posicion[0] + dx
            nueva_y = self.posicion[1] + dy
            if self.validar_movimiento((nueva_x, nueva_y)):
                actuales.append((nueva_x, nueva_y))
        return actuales