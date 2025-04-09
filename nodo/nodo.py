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

class Reina(Nodo):
    def __init__(self, posicion):
        super().__init__(posicion)  # Posición como tupla (fila, columna)

    def mover(self, destino):
        if self.validar_movimiento(destino):
            self.posicion = destino
            return f"Reina a {destino}"
        return None

    def validar_movimiento(self, destino):
        # Solo chequeamos límites aquí; la lógica de ataque va en el algoritmo
        fila, col = destino
        return 0 <= fila < 8 and 0 <= col < 8  # Ajustaremos según N dinámico