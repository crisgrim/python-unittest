import unittest

from model.Geometria import Geometria


class TestGeometria(unittest.TestCase):

    def setUp(self):
        self.g = Geometria(2.00, 3.10, 4.00)

    def test_areaCuadrado(self):
        self.assertEqual(self.g.areaCuadrado(2), 4)
        self.assertEqual(self.g.areaCuadrado(-2), 4)
        self.assertEqual(self.g.areaCuadrado(0), 0)
        self.assertEqual(self.g.areaCuadrado(1), 1)

    def test_areaCirculo(self):
        self.assertEqual(self.g.areaCirculo(2), 12.5664)
        self.assertEqual(self.g.areaCirculo(-2), 12.5664)
        self.assertEqual(self.g.areaCirculo(0), 0)
        self.assertEqual(self.g.areaCirculo(1), 3.1416)

    def test_areaTiangulo(self):
        self.assertEqual(self.g.areaTiangulo(2, 2), 2.0)
        self.assertEqual(self.g.areaTiangulo(-2, -2), 2.0)
        self.assertEqual(self.g.areaTiangulo(0, 0), 0)
        self.assertEqual(self.g.areaTiangulo(1, 1), 0.5)

    def test_areaRectangulo(self):
        self.assertEqual(self.g.areaRectangulo(2, 2), 4)
        self.assertEqual(self.g.areaRectangulo(-2, -2), 4)
        self.assertEqual(self.g.areaRectangulo(0, 0), 0)
        self.assertEqual(self.g.areaRectangulo(1, 1), 1)

    def test_areaPentagono(self):
        self.assertEqual(self.g.areaPentagono(2, 2), 2.0)
        self.assertEqual(self.g.areaPentagono(-2, -2), 2.0)
        self.assertEqual(self.g.areaPentagono(0, 0), 0)
        self.assertEqual(self.g.areaPentagono(1, 1), 0.5)

    def test_areaRombo(self):
        self.assertEqual(self.g.areaRombo(2, 2), 2.0)
        self.assertEqual(self.g.areaRombo(-2, -2), 2.0)
        self.assertEqual(self.g.areaRombo(0, 0), 0)
        self.assertEqual(self.g.areaRombo(1, 1), 0.5)

    def test_areaRomboide(self):
        self.assertEqual(self.g.areaRomboide(2, 2), 4)
        self.assertEqual(self.g.areaRomboide(-2, -2), 4)
        self.assertEqual(self.g.areaRomboide(0, 0), 0)
        self.assertEqual(self.g.areaRomboide(1, 1), 1)

    def test_areaTrapecio(self):
        self.assertEqual(self.g.areaRomboide(2, 2), 4)
        self.assertEqual(self.g.areaRomboide(-2, -2), 4)
        self.assertEqual(self.g.areaRomboide(0, 0), 0)
        self.assertEqual(self.g.areaRomboide(1, 1), 1)

    def test_set_figuraName(self):
        results = ['Cuadrado', 'Circulo', 'Tiangulo', 'Rectangulo', 'Pentagono', 'Rombo', 'Romboide', 'Trapecio']
        for index, result in enumerate(results):
            self.g.set_figuraName(index + 1)
            self.assertEqual(self.g.figuraName, result)

    def test_switch(self):
        results = [4.0, 12.5664, 3.1, 6.2, 3.1, 3.1, 6.2, 10.2]
        for index, result in enumerate(results):
            sw = self.g.switch(index + 1)
            self.assertEqual(sw, result)


if __name__ == '__main__':
    unittest.main()
