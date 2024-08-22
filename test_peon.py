import unittest

class Peon:
    def __init__(self, color):
        self.__color__ = color

    def mov(self, position_actual):
        x, y = position_actual
        movimientos = []
        direccion = 1 if self.__color__ == "blanco" else -1

        if 0 <= y + direccion <= 7:
            movimientos.append((x, y + direccion))

        #
        if (y == 1 and self.__color__ == "blanco") or (y == 6 and self.__color__ == "negro"):
            if 0 <= y + 2 * direccion <= 7:
                movimientos.append((x, y + 2 * direccion))

        return movimientos

    
    
class TestPeon(unittest.TestCase):

    def test_mov_peon_blanco_inicial(self):
        peon_blanco = Peon("blanco")
        movimientos = peon_blanco.mov((4, 1))
        self.assertEqual(movimientos, [(4, 2), (4, 3)])

    def test_mov_peon_blanco_medio(self):
        peon_blanco = Peon("blanco")
        movimientos = peon_blanco.mov((4, 3))
        self.assertEqual(movimientos, [(4, 4)])

    def test_mov_peon_negro_inicial(self):
        peon_negro = Peon("negro")
        movimientos = peon_negro.mov((4, 6))
        self.assertEqual(movimientos, [(4, 5), (4, 4)])

    def test_mov_peon_negro_medio(self):
        peon_negro = Peon("negro")
        movimientos = peon_negro.mov((4, 4))
        self.assertEqual(movimientos, [(4, 3)])

if __name__ == "__main__":
    unittest.main()
