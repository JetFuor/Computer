class Pizza:
    def __init__(self, width, price):
        self.width = width
        self.price = price

    def hascheese(self):
        return True

    def toppings(self):
        return ("None")

class Pepperoni(Pizza):
    def __init__(self, width, price):
        super().__init__(width, price)

    def toppings(self):
        return ("Pepperoni")

    def spicy(self):
        print("Yes a bit.")

class Caesar(Pizza):
    def __init__(self, width, price):
        super().__init__(width, price)

    def toppings(self):
        return ("Artichoke, Feta, Olives")

    def rome(self):
        print("Probably not Roman")

class Chicago(Pizza):
    def __init__(self, width, price):
        super().__init__(width, price)

    def height(self):
        return 4

class ChicagoPepperoni(Chicago, Pepperoni):
    def __init__(self, width, price):
        super().__init__(width, price)

    def toppings(self):
        return ("Pepperoni, not enough cheese")

    def available(self):
        if self.width > 10:
            return ("Not available")

Shalit_fav = Pepperoni(14, 100)
print(Shalit_fav.toppings())
print(Shalit_fav.hascheese())

Stephen_fav = ChicagoPepperoni(11, 500)
print(Stephen_fav.available())
print(Stephen_fav.toppings())
print(Stephen_fav.height())