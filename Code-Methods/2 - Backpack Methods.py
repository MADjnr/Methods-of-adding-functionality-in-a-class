"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items



## build a class of Backpack
## build its constructor
##since the item is protected, use a property to build it getter
## build a add_item method
##   check if the item is string and append item inside it
##build a remove_item method
##   check if item is in the Backpack, if yes, remove it
##build a method to check if an item in in the backpack


class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    ## define a method to add item inside the Backpack
    ## we want to be able to add item inside the Backpack
    def add_item(self, item):
       ## to check if the item is a string
        if isinstance(item, str):
            self._items.append(item)

        else:
            print('Please provide a valid item')
     ## we have to specify the item that we want to remove
    def remove_item(self, item):
        if item in self._items:  ##if the item is in the list of items of the Backpack instance
            self._items.remove(item) ## we remove that item
            return 1
        else:
            return 0

    def has_item(self, item):
        ## so this method returns an item if it finds it
        return item in self._items ## return true if the item is in the list of items else it will return false.