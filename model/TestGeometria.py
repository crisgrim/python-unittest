import unittest

from model.Geometria import Geometria


class TestGeometria(unittest.TestCase):

    # def setUp(self):
    #     g = Geometria(2.00, 3.10, 4.00)
    #     self.assertEqual()

    def test_areaCuadrado(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaCuadrado(2), 4)
        self.assertEqual(g.areaCuadrado(-2), 4)
        self.assertEqual(g.areaCuadrado(0), 0)
        self.assertEqual(g.areaCuadrado(1), 1)

    def test_areaCirculo(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaCirculo(2), 12.5664)
        self.assertEqual(g.areaCirculo(-2), 12.5664)
        self.assertEqual(g.areaCirculo(0), 0)
        self.assertEqual(g.areaCirculo(1), 3.1416)

    def test_areaTiangulo(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaTiangulo(2, 2), 2.0)
        self.assertEqual(g.areaTiangulo(-2, -2), 2.0)
        self.assertEqual(g.areaTiangulo(0, 0), 0)
        self.assertEqual(g.areaTiangulo(1, 1), 0.5)

    def test_areaRectangulo(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaRectangulo(2, 2), 4)
        self.assertEqual(g.areaRectangulo(-2, -2), 4)
        self.assertEqual(g.areaRectangulo(0, 0), 0)
        self.assertEqual(g.areaRectangulo(1, 1), 1)

    def test_areaPentagono(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaPentagono(2, 2), 2.0)
        self.assertEqual(g.areaPentagono(-2, -2), 2.0)
        self.assertEqual(g.areaPentagono(0, 0), 0)
        self.assertEqual(g.areaPentagono(1, 1), 0.5)

    def test_areaRombo(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaRombo(2, 2), 2.0)
        self.assertEqual(g.areaRombo(-2, -2), 2.0)
        self.assertEqual(g.areaRombo(0, 0), 0)
        self.assertEqual(g.areaRombo(1, 1), 0.5)

    def test_areaRomboide(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaRomboide(2, 2), 4)
        self.assertEqual(g.areaRomboide(-2, -2), 4)
        self.assertEqual(g.areaRomboide(0, 0), 0)
        self.assertEqual(g.areaRomboide(1, 1), 1)

    def test_areaTrapecio(self):
        g = Geometria(2.00, 3.10, 4.00)
        self.assertEqual(g.areaRomboide(2, 2), 4)
        self.assertEqual(g.areaRomboide(-2, -2), 4)
        self.assertEqual(g.areaRomboide(0, 0), 0)
        self.assertEqual(g.areaRomboide(1, 1), 1)

    def test_set_figuraName(self):
        g = Geometria(2.00, 3.10, 4.00)
        results = ['Cuadrado', 'Circulo', 'Tiangulo', 'Rectangulo', 'Pentagono', 'Rombo', 'Romboide', 'Trapecio']
        for index, result in enumerate(results):
            g.set_figuraName(index + 1)
            self.assertEqual(g.figuraName, result)

    def test_switch(self):
        g = Geometria(2.00, 3.10, 4.00)
        results = [4.0, 12.5664, 3.1, 6.2, 3.1, 3.1, 6.2, 10.2]
        for index, result in enumerate(results):
            sw = g.switch(index + 1)
            self.assertEqual(sw, result)


if __name__ == '__main__':
    unittest.main()
