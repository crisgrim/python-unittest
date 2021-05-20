import unittest
from unittest.mock import patch

from model.Geometria import Geometria
from view.View import View

figuras = ['Cuadrado', 'Circulo', 'Triangulo', 'Rectangulo', 'Pentagono', 'Rombo', 'Romboide', 'Trappecio']
areas = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
opciones = ['1', '2', '3', '4', '5', '6', '7', '8']


class TestView(unittest.TestCase):

    @patch('builtins.input', side_effect=opciones)
    def test_select(self, mock_input):
        g = Geometria(2.00, 3.10, 4.00)
        v = View()
        area = v.select(g)
        figura = g.figuraName

        # Así funciona
        self.assertEqual(figura, 'Cuadrado')
        self.assertEqual(area, 4.0)

        # Pero yo quiero hacerlo dinámico
        # Algo así, con un index
        # self.assertEqual(figura, figuras[index])
        # self.assertEqual(area, areas[index])


for figura in figuras:
    test = TestView()
    result = test.test_select()


if __name__ == '__main__':
    unittest.main()
