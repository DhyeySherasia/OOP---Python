import math

"""

All the data types in python are made from class. Then too they can be added by a '+' sign.
Similarly we can also add objects of our own class with a '+' sign.
def __add__(first_object, second_object):
    return (first_object.__radius + second_object.__radius)
    
"""


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * pow(self.__radius, 2)

    # Takes two objects as input arguments
    def __add__(self, other_object):
        # returning the class Circle(added_radius) to c3. Hence can use c3.get_radius()
        # Can also do without returning class circle. But then will not be able to use get_radius()
        return Circle(self.__radius + other_object.__radius)

    def __lt__(self, other_object):
        return self.__radius < other_object.__radius

    def __gt__(self, other_object):
        return self.__radius > other_object.__radius

    def __str__(self):
        return "Area of this circle = " + str(self.area())


c1 = Circle(2)
c2 = Circle(3)

c3 = c1 + c2  # + sign is overloaded as __add__ method
print(c3.get_radius())
c4 = c1.__add__(c2)  # self.__add__(other_object)
print(c4.get_radius())

print(c1 > c2)

# Other data types are also overloaded in similar manner
a = 5
b = 10
print(a.__add__(b))
print(str(c1))
