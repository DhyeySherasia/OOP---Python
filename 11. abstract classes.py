from abc import ABC, abstractmethod


# Making any method of the class as abstract makes the class also abstract.
# Now we cannot instantiate the class, cannot create an object of this class
class Shape(ABC):

    # abstract method is the method which you 'must implement' in the sub class
    @abstractmethod
    def area(self):
        pass

    # @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side


shape1 = Square(5)
