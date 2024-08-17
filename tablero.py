from chess import Chess


def play(chess):    
    try:
        print(chess.show_board())
        from_row = int(input("From_row: "))
        from_col = int(input("From_col: "))
        to_row = int(input("To_row: "))
        to_col = int(input("To_col: "))
    
    except Exception as e:
        print("error")
    
    
    chess.move(
        from_row,
        from_col,
        to_row,
        to_col,
    )