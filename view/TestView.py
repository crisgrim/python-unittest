import unittest
from unittest.mock import patch

from model.Geometria import Geometria
from view.View import View

opciones = ['1', '2', '3', '4', '5', '6', '7', '8']


class TestView(unittest.TestCase):

    @patch('builtins.input', side_effect=opciones)
    def test_select(self, mock_input):
        g = Geometria(2.00, 3.10, 4.00)
        v = View()
        area = v.select(g)
        figura = g.figuraName

        self.assertEqual(figura, 'Cuadrado')
        self.assertEqual(area, 4.0)


if __name__ == '__main__':
    unittest.main()
