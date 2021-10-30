class Polygon:
    __height = None
    __width = None

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    # private member variables cannot be accessed normally in subclass. Hence use getter:
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()


class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() / 2


rect = Rectangle()
rect.set_values(10, 5)
print(rect.area())

tri = Triangle()
tri.set_values(10, 5)
print(tri.area())
