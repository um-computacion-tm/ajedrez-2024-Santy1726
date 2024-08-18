import unittest
from pieces import Rook
from your_module import Board  # Asegúrate de reemplazar 'your_module' con el nombre del archivo donde está la clase Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_pieces(self):
        # Prueba las piezas en las posiciones esperadas
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
        
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
        
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")

    def test_empty_positions(self):
        # Prueba posiciones que deben estar vacías
        for row in range(8):
            for col in range(8):
                if (row, col) not in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                    self.assertIsNone(self.board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()
