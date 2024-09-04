import unittest
from Piezas.rook import Rook  # Asegúrate de que esta importación sea correcta según tu estructura de archivos

class TestRook(unittest.TestCase):

    def setUp(self):
        # Configurar la instancia de Rook para ser usada en los tests
        self.__rook__ = Rook((4, 4), "WHITE")

    def test_movimientos_rook_desde_centro(self):
        self.__rook__.__posicion_actual__ = (4, 4)
        movimientos_validos = self.__rook__.__calcular_movimientos_validos__()
        movimientos_esperados = [
            (5, 4), (6, 4), (7, 4),  # Movimientos hacia la derecha
            (3, 4), (2, 4), (1, 4), (0, 4),  # Movimientos hacia la izquierda
            (4, 5), (4, 6), (4, 7),  # Movimientos hacia arriba
            (4, 3), (4, 2), (4, 1), (4, 0)   # Movimientos hacia abajo
        ]
        self.assertEqual(sorted(movimientos_validos), sorted(movimientos_esperados))

    def test_movimientos_rook_desde_esquina(self):
        self.__rook__.__posicion_actual__ = (0, 0)
        movimientos_validos = self.__rook__.__calcular_movimientos_validos__()
        movimientos_esperados = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Movimientos hacia la derecha
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Movimientos hacia arriba
        ]
        self.assertEqual(sorted(movimientos_validos), sorted(movimientos_esperados))

    def test_rook_bloqueada_por_mismo_color(self):
        # Supongamos que hay piezas del mismo color en las posiciones (5, 4) y (4, 5)
        self.__rook__.__posicion_actual__ = (4, 4)
        
        def mock_obtener_pieza_en_posicion(x, y):
            if (x, y) in [(5, 4), (4, 5)]:
                return Rook((x, y), "WHITE")
            return None
        
        self.__rook__.__obtener_pieza_en_posicion__ = mock_obtener_pieza_en_posicion
        movimientos_validos = self.__rook__.__calcular_movimientos_validos__()
        movimientos_esperados = [
            (3, 4), (2, 4), (1, 4), (0, 4),  # Movimientos hacia la izquierda
            (4, 3), (4, 2), (4, 1), (4, 0)   # Movimientos hacia abajo
        ]
        self.assertEqual(sorted(movimientos_validos), sorted(movimientos_esperados))

if __name__ == "__main__":
    unittest.main()


   