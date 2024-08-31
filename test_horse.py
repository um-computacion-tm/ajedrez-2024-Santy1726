import unittest

from Piezas.horse import Horse

class TestHorse(unittest.TestCase):

    def test_str(self):
        caballo_blanco = Horse("WHITE")
        caballo_negro = Horse("BLACK")
        self.assertEqual(str(caballo_blanco), "♘")
        self.assertEqual(str(caballo_negro), "♞")

    def test_mov_del_horse(self):
        caballo = Horse("WHITE")
        
        # Test en la esquina inferior izquierda
        posicion_actual = (0, 0)
        movimientos_esperados = [(2, 1), (1, 2)]
        self.assertEqual(caballo.mov_del_horse(posicion_actual), movimientos_esperados)

        # Ahora ubicado en una posicion Central
        posicion_actual = (4, 4)
        movimientos_esperados = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        self.assertEqual(caballo.mov_del_horse(posicion_actual), movimientos_esperados)

        # Ubicado en la esquina superior derecha 
        posicion_actual = (7, 7)
        movimientos_esperados = [(5, 6), (6, 5)]
        self.assertEqual(caballo.mov_del_horse(posicion_actual), movimientos_esperados)


    def test_mov_del_horse(self):
        caballo = Horse("BLACK")
    
    # Test en la esquina superior izquierda
        posicion_actual = (7, 0)
        movimientos_esperados = [(5, 1), (6, 2)]
        self.assertEqual(caballo.mov_del_horse(posicion_actual), movimientos_esperados)

    # Ubicado en una posición central diferente
        posicion_actual = (3, 3)
        movimientos_esperados = [
        (5, 4), (5, 2), (1, 4), (1, 2),
        (4, 5), (4, 1), (2, 5), (2, 1)
    ]
        self.assertEqual(caballo.mov_del_horse(posicion_actual), movimientos_esperados)

    # Ubicado en la esquina inferior derecha
        posicion_actual = (0, 7)
        movimientos_esperados = [(2, 6), (1, 5)]
        self.assertEqual(caballo.mov_del_horse(posicion_actual), movimientos_esperados)



if __name__ == '__main__':
    unittest.main()





