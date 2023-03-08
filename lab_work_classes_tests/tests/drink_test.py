import unittest
from src.drink import Drink
from src.food import Food

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Beer", 6.00, 2)
    
    def test_has_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_has_price(self):
        self.assertEqual(6.00, self.drink.price)