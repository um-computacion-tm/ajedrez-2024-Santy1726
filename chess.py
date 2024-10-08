from board import Board

class chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = 'WHITE'

    def move (
        self, 
        from_row,
        from_col,
        to_row,
        to_col,
    ):  
        
        píece = self.board.get_piece(from_row, from_col)
        self.change_turn()

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
