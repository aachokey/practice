# Modules, Classes, and Objects
import mystuff

# Access mystuff.py as a module
mystuff.apple()
print(mystuff.tangerine)

mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable	


# Create a class
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# Call the class like a function
thing = MyStuff() # "instantiate" the operation, which just means create it
thing.apple()
print(thing.tangerine)