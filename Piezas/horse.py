class Horse:

    def __init__(self, color):
        self.color = color

    def __str__(self):
        if self.color == "WHITE":
            return "♘"      # símbolo para el caballo blanco
        else:
            return "♞"      # símbolo para el caballo negro


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