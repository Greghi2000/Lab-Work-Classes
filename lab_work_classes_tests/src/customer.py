class Customer:
    def __init__(self, name, age, wallet, drunkness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = 0
        self.drinks = []

    def add_drink(self, drink_to_buy):
        self.drinks.append(drink_to_buy)

    def count_drinks(self):
        return len(self.drinks)
    
    def count_wallet(self):
        return self.wallet
    
    def reduce_wallet(self, amount):
        self.wallet -= amount

    def how_drunk(self, drink):
        alc_lvl_drink = drink.alc_lvl
        self.drunkness += alc_lvl_drink

    def customer_bought_food(self, food):
        self.drunkness -= food.rejuvenation_level