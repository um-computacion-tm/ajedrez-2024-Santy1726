class Horse:

    def __init__(self, color):
        self.color = color

    def __str__(self):
        if self.color == "WHITE":
            return "♘"      # símbolo para el caballo blanco
        else:
            return "♞"      # símbolo para el caballo negro


    def esta_dentro_del_tablero(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def esta_ocupada_por_mismo_color(self, x, y):
        pieza = self.__obtener_pieza_en_posicion__(x, y)
        return pieza is not None and pieza.__color__ == self.__color__

    def esta_ocupada(self, x, y):
        pieza = self.__obtener_pieza_en_posicion__(x, y)
        return pieza is not None

    def obtener_pieza_en_posicion(self, x, y):
        pass

    def __calcular_movimientos_validos(self):
        movimientos_validos = []
        x, y = self.__posicion_actual__

    def mov_del_horse(self, posicion_actual):
        fila_actual, columna_actual = posicion_actual
        movimientos = [
            (fila_actual + 2, columna_actual + 1),
            (fila_actual + 2, columna_actual - 1),
            (fila_actual - 2, columna_actual + 1),
            (fila_actual - 2, columna_actual - 1),
            (fila_actual + 1, columna_actual + 2),
            (fila_actual + 1, columna_actual - 2),
            (fila_actual - 1, columna_actual + 2),
            (fila_actual - 1, columna_actual - 2)
        ]

        mov_validos = [
            (fila, columna) for fila, columna in movimientos
            if 0 <= fila < 8 and 0 <= columna < 8
        ]

        return mov_validos