class Car:

    # Called when an object is assigned
    def __init__(abc, mileage, speed, colour):
        print("__init__ is called")
        print("Mileage is " + str(mileage))
        abc.car_speed = speed
        abc.colour = colour
        abc.mileage = mileage


# audi, bmw etc are objects
audi = Car(18.5, 250, 'silver')
bmw = Car(21.3, 200, 'matt black')
mercedes = Car(20.5, 230, 'white')

# Can add attributes on the go
# audi.speed = 250
# bmw.speed = 200
# mercedes.speed = 230

# speed and colour are variables which hold some data inside them
audi.colour = "silver"
bmw.colour = "matt black"
mercedes.colour = "white"

print(mercedes.colour)
print(mercedes.car_speed)
print(mercedes.mileage)
