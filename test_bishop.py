
import unittest
from board import Board
from Piezas.bishop import Bishop

class TestBishop(unittest.TestCase):

    def test_mov_del_bishop_centro(self):
        tablero = Board()
        bishop = Bishop(4, 4, 'blanco')
        movimientos_esperados = [
            (3, 3), (2, 2), (1, 1), (0, 0),  # diagonal superior izquierda
            (3, 5), (2, 6), (1, 7),          # diagonal superior derecha
            (5, 3), (6, 2), (7, 1),          # diagonal inferior izquierda
            (5, 5), (6, 6), (7, 7)           # diagonal inferior derecha
        ]
        resultado = bishop.mov((4, 4), tablero)
        self.assertEqual(sorted(resultado), sorted(movimientos_esperados))

    def test_mov_del_bishop_esquina_inferior_izquierda(self):
        tablero = Board()
        bishop = Bishop(0, 0, 'blanco')
        movimientos_esperados = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  # diagonal hacia abajo-derecha
        ]
        resultado = bishop.mov((0, 0), tablero)
        self.assertEqual(sorted(resultado), sorted(movimientos_esperados))

    def test_mov_del_bishop_bloqueo_pieza_propia(self):
        tablero = Board()
        tablero.colocar_pieza(Bishop(3, 3, 'blanco'))  # Bloqueo en diagonal superior izquierda
        bishop = Bishop(4, 4, 'blanco')
        movimientos_esperados = [
            (3, 5), (2, 6), (1, 7),  # diagonal superior derecha
            (5, 3), (6, 2), (7, 1),  # diagonal inferior izquierda
            (5, 5), (6, 6), (7, 7)   # diagonal inferior derecha
        ]
        resultado = bishop.mov((4, 4), tablero)
        self.assertEqual(sorted(resultado), sorted(movimientos_esperados))

    def test_mov_del_bishop_bloqueo_pieza_contraria(self):
        tablero = Board()
        tablero.colocar_pieza(Bishop(3, 5, 'negro'))  # Bloqueo en diagonal superior derecha
        bishop = Bishop(4, 4, 'blanco')
        movimientos_esperados = [
            (3, 5), (2, 6), (1, 7),  # diagonal superior derecha hasta la pieza negra
            (5, 3), (6, 2), (7, 1),  # diagonal inferior izquierda
            (5, 5), (6, 6), (7, 7)   # diagonal inferior derecha
        ]
        resultado = bishop.mov((4, 4), tablero)
        self.assertEqual(sorted(resultado), sorted(movimientos_esperados))

if __name__ == '__main__':
    unittest.main()

