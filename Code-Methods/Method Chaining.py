class Pizza:

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self ## The last line is what allows method chaining.
        # It returns self (the instance that called the method),
        # so you can use it to call another method in the same line

    def display_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())
            return self.toppings


pizza = Pizza()

print(pizza.add_topping('chocolate pie').add_topping('vanilla honey').add_topping('milkshake').\
      add_topping('Alovera cream') \
.display_toppings())

