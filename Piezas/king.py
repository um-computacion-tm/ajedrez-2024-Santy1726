class King:

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♚"
        else:
            return "♔"

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
        pass  # Aquí iría el código que interactúa con el tablero para obtener la pieza en una posición

    def __calcular_movimientos_validos__(self):
        movimientos_validos = []
        x, y = self.__posicion_actual__

        # Los 8 movimientos posibles del rey
        posibles_movimientos = [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1),           (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]

        for nuevo_x, nuevo_y in posibles_movimientos:
            if self.__esta_dentro_del_tablero__(nuevo_x, nuevo_y) and not self.__esta_ocupada_por_mismo_color__(nuevo_x, nuevo_y):
                movimientos_validos.append((nuevo_x, nuevo_y))

        return movimientos_validos

