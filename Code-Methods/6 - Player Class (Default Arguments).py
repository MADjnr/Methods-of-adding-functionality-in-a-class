"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change


my_player = Player(5, 10)

my_player.move_up()
print(my_player.y)

my_player.move_up(8)
print(my_player.y)

my_player.move_down()
print(my_player.y)

my_player.move_down(3)
print(my_player.y)

my_player.move_right()
print(my_player.x)

my_player.move_right(1)
print(my_player.x)

my_player.move_left()
print(my_player.x)

my_player.move_left(10)
print(my_player.x)
'''

## create a class of Player
## design a constructor--- The instance attributes are public
## design a method for movement in the Y dirction why retaining a default argument of 5
## repeat this design for movements down, right and left

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move_up(self, change = 7):
        self.y += change

    def move_down(self, change =9):
        self.y -= change

    def move_right(self, change = 6):
        self.x += change

    def move_left(self, change = 6):
        self.x -= change

my_player = Player(12,30)

my_player.move_up()
print(my_player.y)

my_player.move_up()
print(my_player.y)

my_player.move_down(20)
print(my_player.y)

my_player.move_right()
print(my_player.x)

my_player.move_left(23)
print(my_player.x)