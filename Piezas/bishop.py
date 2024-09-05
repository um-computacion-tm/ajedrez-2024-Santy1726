class Bishop:
    def __init__(self, fila, columna, color):
        self.fila = fila
        self.columna = columna
        self.color = color

    def mov(self, posicion, tablero):
        fila, columna = posicion
        movimientos_validos = []

        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Explorar cada dirección
        for direccion in direcciones:
            dx, dy = direccion
            x, y = fila + dx, columna + dy

          
            while 0 <= x < 8 and 0 <= y < 8:
                # Si la casilla está ocupada
                if tablero.esta_ocupada(x, y):
                    # Si es una pieza del color contrario, agregar como movimiento válido
                    if not tablero.esta_ocupada_por_mismo_color(x, y, self.color):
                        movimientos_validos.append((x, y))
                    break
                else:
                    movimientos_validos.append((x, y))
                
                # Avanzar en la misma dirección
                x += dx
                y += dy

        return movimientos_validos



    