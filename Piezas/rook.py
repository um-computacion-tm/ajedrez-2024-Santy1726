class Rook:

    def __str__(self):

        if self.__color__ == "WHITE":

            return "♜"

        else:

            return "♖"



    def __init__(self, current_position, color):
        self.current_position = current_position
        self.color = color
    

    def calculate_valid_moves(self):
        valid_moves = []
        x, y = self.current_position
        
        # Movimiento horizontal hacia la derecha
        for i in range(x + 1, 8):
            if self.is_within_board(i, y) and not self.is_occupied_by_same_color(i, y):
                valid_moves.append((i, y))
            if self.is_occupied(i, y):
                break
        
        # Movimiento horizontal hacia la izquierda
        for i in range(x - 1, -1, -1):
            if self.is_within_board(i, y) and not self.is_occupied_by_same_color(i, y):
                valid_moves.append((i, y))
            if self.is_occupied(i, y):
                break

        # Movimiento vertical hacia arriba
        for j in range(y + 1, 8):
            if self.is_within_board(x, j) and not self.is_occupied_by_same_color(x, j):
                valid_moves.append((x, j))
            if self.is_occupied(x, j):
                break

        # Movimiento vertical hacia abajo
        for j in range(y - 1, -1, -1):
            if self.is_within_board(x, j) and not self.is_occupied_by_same_color(x, j):
                valid_moves.append((x, j))
            if self.is_occupied(x, j):
                break

        return valid_moves


