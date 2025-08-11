from Vehicle import Vehicle

class Plane(Vehicle):
    def move(self):
        print("fly")

Plane1 = Plane("Titanic", "Black")

print(Plane1.color)
print(Plane1.brand)
Plane1.move()