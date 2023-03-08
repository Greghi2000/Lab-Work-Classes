import unittest
from src.customer import Customer
from src.drink import Drink, LongIsland
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Murray", 23, 50, 0)

    def test_customer_has_name(self):
        self.assertEqual("Murray", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_add_drink_customer(self):
        drink_bought = Drink("Long Island", 10.99, 5)
        self.customer.add_drink(drink_bought)
        self.assertEqual(1, self.customer.count_drinks())

    def test_how_drunk(self):
        # drink_bought = Drink("Long Island", 10.99, 5)
        drink_bought = LongIsland()
        self.customer.how_drunk(drink_bought)
        self.assertEqual(6, self.customer.drunkness)

    def test_customer_bought_food(self):
        food_bought = Food("Curry", 12.99, 5)
        self.customer.customer_bought_food(food_bought)
        self.assertEqual(-5, self.customer.drunkness)

    def test_lvl_of_accptl(self):
        pass