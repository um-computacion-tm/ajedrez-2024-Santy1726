class Horse:

    def __init__(self, color):
        self.color = color

    def __str__(self):
        if self.color == "WHITE":
            return "♘"  # símbolo para el caballo blanco
        else:
            return "♞"  # símbolo para el caballo negro
