from Vehicle import Vehicle

class Boat(Vehicle):
    def move(self):
        print("Sail")

boat1 = Boat("Titanic", "Black")

print(boat1.color)
print(boat1.brand)
boat1.move()