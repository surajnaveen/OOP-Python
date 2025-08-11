from Vehicle import Vehicle

class Car(Vehicle):
    pass

Car1 = Car("Volvo", "Blue")

print(Car1.brand + " , " + Car1.color)
Car1.move()