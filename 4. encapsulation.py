"""

self.a    -->  can access an change outside class
self._b   -->  semi-private
self.__c  -->  truly private. Cannot access outside the class
Truly private member variables cannot be accessed even in subclasses via inheritance

"""


class Car:
    def __init__(self, speed, colour):
        self.__speed = speed
        self.colour = colour

    # can manipulate attributes defined under __init__
    # cannot add new attributes in such methods
    def set_speed(self, updated_speed):
        self.__speed = updated_speed

    def get_speed(self):
        return self.__speed

    # private methods similar to private attribute variables
    def __private_method(self):
        print("private method")


audi = Car(230, 'white')
bmw = Car(250, 'matt black')
mercedes = Car(300, 'silver')

# cannot change the value of speed. Change using audi.set_speed()
audi.__speed = 1000

# can change colour as it is not private
audi.colour = "new colour"

print(audi.colour)
print(audi.get_speed())
