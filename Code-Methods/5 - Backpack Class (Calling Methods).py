"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
'''
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
            print("This item is not in the backpack.")
            return 0

    def has_item(self, item):
        return item in self._items


my_backpack = Backpack()

print(my_backpack.items)
my_backpack.add_item("Water Bottle")

print(my_backpack.items)

my_backpack.add_item("Sleeping Bag")
print(my_backpack.items)

has_water = my_backpack.has_item("Water Bottle")
print(has_water)

my_backpack.remove_item("Water Bottle")
print(my_backpack.items)

my_backpack.remove_item("Sleeping Bag")
print(my_backpack.items)

my_backpack.remove_item("Candy")
print(my_backpack.items)
'''

### create Toolbox class
##build its constructor
## protect the instance attribut- items and assign it to an empty list
## build a decorator with the property so you can get it everytime
##build a method to add a tool in the list of tools
##  check if the tool is an int if yes, append it to the list of items in the tool box
##  if not, print a message for someone to provide a valid item
##Build the method to remove an item
##  if item is in the instance attribute, use remove method of a list on it
##   then return 1
##    else, print that the item is not in the toolbox and then return 0
##Build a method to check if an Toolbox as an item---bool



class Toolbox:


    def __init__(self):
        self._tools = []

    @property
    def tools(self):
        return self._tools

    ## a method to add tools inside the toolbox
    ## i will check if the tool is an int
    ## then if yes, append it in the value of the instance attribute
    ## if not print a message for someone to provide the correct tool
    def add_tool(self, tool):
        if isinstance(tool, str):
            self._tools.append(tool)

        else:
            print('Kindly provide the right tool')

    ##Build a method to remove a tool from the toolbox
    ##conditional to check if item is in
    ##if satisfied, remove it
    ## return 1
    ## else, print that the item is not in the toolbox
    ## then return 0

    def remove_tool(self, tool):
        if tool in self._tools:
            self._tools.remove(tool)
            return 1

        else:
            print('The tool cannot be found in the toolbox')
            return 0

    def has_tool(self, tool):
        return tool in self._tools


my_tools = Toolbox()

print(my_tools.tools)

my_tools.add_tool('Hammer')
print(my_tools.tools)


my_tools.add_tool('cheasl')
print(my_tools.tools)

my_tools.remove_tool('cheasl')
print(my_tools.tools)

check1 = my_tools.has_tool('hammer')
print(check1)

check2 = my_tools.has_tool('Hammer')
print(check2)