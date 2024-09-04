class Rook:

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"

    def __init__(self, posicion_actual, color):
        self.__posicion_actual__ = posicion_actual
        self.__color__ = color

    def __esta_dentro_del_tablero__(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def __esta_ocupada_por_mismo_color__(self, x, y):
        pieza = self.__obtener_pieza_en_posicion__(x, y)
        return pieza is not None and pieza.__color__ == self.__color__

    def __esta_ocupada__(self, x, y):
        pieza = self.__obtener_pieza_en_posicion__(x, y)
        return pieza is not None

    def __obtener_pieza_en_posicion__(self, x, y):
        # Este método debería interactuar con el tablero para obtener la pieza en la posición (x, y)
        pass

    def __calcular_movimientos_validos__(self):
        movimientos_validos = []
        x, y = self.__posicion_actual__
        
        # Movimiento horizontal hacia la derecha
        for i in range(x + 1, 8):
            if self.__esta_dentro_del_tablero__(i, y) and not self.__esta_ocupada_por_mismo_color__(i, y):
                movimientos_validos.append((i, y))
            if self.__esta_ocupada__(i, y):
                break
        
        # Movimiento horizontal hacia la izquierda
        for i in range(x - 1, -1, -1):
            if self.__esta_dentro_del_tablero__(i, y) and not self.__esta_ocupada_por_mismo_color__(i, y):
                movimientos_validos.append((i, y))
            if self.__esta_ocupada__(i, y):
                break

        # Movimiento vertical hacia arriba
        for j in range(y + 1, 8):
            if self.__esta_dentro_del_tablero__(x, j) and not self.__esta_ocupada_por_mismo_color__(x, j):
                movimientos_validos.append((x, j))
            if self.__esta_ocupada__(x, j):
                break

        # Movimiento vertical hacia abajo
        for j in range(y - 1, -1, -1):
            if self.__esta_dentro_del_tablero__(x, j) and not self.__esta_ocupada_por_mismo_color__(x, j):
                movimientos_validos.append((x, j))
            if self.__esta_ocupada__(x, j):
                break

        return movimientos_validos
