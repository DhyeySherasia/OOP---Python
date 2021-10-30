class Rectangle:
    pass


rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = 30
rect1.width = 10

rect2.height = 5
rect2.width = 10

rect1.area = rect1.height * rect1.width
rect2.area = rect2.height * rect2.width

print(rect2.area)

