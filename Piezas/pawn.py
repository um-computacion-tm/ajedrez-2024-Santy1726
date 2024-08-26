
class Peon:
    
    def mov(self,position_actual):
        
        x, y = position_actual
        mov = []

        if 0 <= y + direccion <= 7:
            mov.append((x, y + direccion))

        if (y == 1 and self.__color__ == "blanco") or (y == 6 and self.__color__ == "negro"):
            if 0 <= y + 2 * direccion <= 7:
                mov.append((x, y + 2 * direccion))

        if row != start_row:
            mov.append((row + direccion, col - 1))
            mov.append((row + direccion, col + 1)) 


        return mov