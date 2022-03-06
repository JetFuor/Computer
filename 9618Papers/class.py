class Pizza():

    attr1 = "food"
    attr2 = "cheese"

    def ingredient(self):
        print("An ingredient is " + self.attr2)
        print("Pizza is a type of " + self.attr1)

class Chicago(Pizza):
    def nocheese(self):
        print("Pizza doesn't have enough " + self.attr2)

Favorite = Chicago()

print(Favorite.attr2)
Favorite.nocheese()
Favorite.ingredient()