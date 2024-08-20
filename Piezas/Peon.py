
class peon:
    def__init__(self, color)
    self.__color___ = color 

def mov(self,position_actual):
        
        x, y = position_actual
        movimientos = []

        if 0 <= y + direccion <= 7:
            movimientos.append((x, y + direccion))

        if (y == 1 and self.__color__ == "blanco") or (y == 6 and self.__color__ == "negro"):
            if 0 <= y + 2 * direccion <= 7:
                movimientos.append((x, y + 2 * direccion))

        return movimientos