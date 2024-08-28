class Peon:
    def __str__(self):

        if self.__color__ == "WHITE":

            return "♙"     # simbolo para el peon blanco

        else:

            return "♟"     # simbolo para el peon negro

    def __init__(self, start_row, start_col, color):
        self.start_row = start_row
        self.start_col = start_col
        self.__color__ = color
    
    def mov(self, position_actual):
        x, y = position_actual
        mov = []
        
        direccion = 1 if self.__color__ == "blanco" else -1

        if 0 <= y + direccion <= 7:
            mov.append((x, y + direccion))

            
            if (self.__color__ == "blanco" and y == 1) or (self.__color__ == "negro" and y == 6):
                if 0 <= y + 2 * direccion <= 7:
                    mov.append((x, y + 2 * direccion))

        for col in [x - 1, x + 1]:
            if 0 <= col <= 7 and 0 <= y + direccion <= 7:
                mov.append((col, y + direccion))

        return mov
