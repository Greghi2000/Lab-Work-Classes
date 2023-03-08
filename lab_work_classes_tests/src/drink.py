class Drink:
    def __init__(self, name, price, alc_lvl):
        self.name = name
        self.price = price
        self.alc_lvl = alc_lvl

class LongIsland(Drink):
    def __init__(self):
        # super().__init__(name, price, alc_lvl)
        self.name = "Long Island"
        self.price = 12.99
        self.alc_lvl = 6