import unittest
from car import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        make='GM'
        model='malibu'
        year=2020
        self.price=40000
        self.km=10000
        self.avto1=Car(make, model, year)
        self.avto2=Car(make, model, year, price=self.price)

    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz.
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymatlar mavjud emasligini assertIsNone metodi bilan tekishiramiz.
        self.assertIsNone(self.avto1.price)
        # Qiymatlar tengligini assertEqual metodi bilan tekshiramiz.
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narhini tekshiramiz.
        self.assertEqual(self.price, self.avto2.price)

    def test_set_price(self):
        new_price=45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)

    def test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000, self.avto1.get_km())
        new_km=-4000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

    def test_get_info(self):
        avto1_info = 'GM Malibu, 2020-yil, 0 km yurgan. '
        self.assertEqual(avto1_info,self.avto1.get_info())


    
        
unittest.main()