from Piezas.bishop import Bishop
from Piezas.horse import Horse
from Piezas.king import King
from Piezas.pawn import Pawn
from Piezas.queen import Queen
from Piezas.rook import Rook


class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

        self.__positions__[0][0] = Rook((0, 0), "BLACK")
        self.__positions__[0][7] = Rook((0, 7), "BLACK")
        self.__positions__[7][0] = Rook((7, 0), "WHITE")
        self.__positions__[7][7] = Rook((7, 7), "WHITE")
        
        self.__positions__[0][2] = Bishop((0, 2), "BLACK")
        self.__positions__[0][5] = Bishop((0, 5), "BLACK")
        self.__positions__[7][2] = Bishop((7, 2), "WHITE")
        self.__positions__[7][5] = Bishop((7, 5), "WHITE")
    
        self.__positions__[0][1] = Horse((0, 1), "BLACK")
        self.__positions__[0][6] = Horse((0, 6), "BLACK")
        self.__positions__[7][1] = Horse((7, 1), "WHITE")
        self.__positions__[7][6] = Horse((7, 6), "WHITE")
        
        self.__positions__[0][4] = King((0, 4), "BLACK")
        self.__positions__[7][4] = King((7, 4), "WHITE")
        
        self.__positions__[0][3] = Queen((0, 3), "BLACK")
        self.__positions__[7][3] = Queen((7, 3), "WHITE")

        for i in range(8):
            self.__positions__[1][i] = Pawn((1, i), "BLACK")
            self.__positions__[6][i] = Pawn((6, i), "WHITE")

    def get_piece(self, row, col):
        return self.__positions__[row][col]




















