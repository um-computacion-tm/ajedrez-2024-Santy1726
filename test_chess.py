
import unittest
from board import Board
from chess import Chess  

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.game.get_turn(), 'WHITE', "El turno inicial no es WHITE")

    def test_move_changes_turn(self):
        
        self.game.move(0, 0, 0, 1)  
        
       
        self.assertEqual(self.game.get_turn(), 'BLACK', "El turno no ha cambiado a BLACK después del movimiento")

    def test_move_updates_board(self):
       
        self.game.move(0, 0, 0, 1)
        
      
        piece_at_destination = self.game.get_board().get_piece(0, 1)
        piece_at_origin = self.game.get_board().get_piece(0, 0)
        
        self.assertIsNotNone(piece_at_destination, "La pieza no se movió correctamente a la posición de destino")
        self.assertIsNone(piece_at_origin, "La pieza no ha sido removida de la posición original")

if __name__ == '__main__':
    unittest.main()
