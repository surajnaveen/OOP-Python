from Class import Vehicle

class Bike(Vehicle):
    def drive(self):
        print("Drive on two wheels")

#Creating a object
bike1 = Bike("Bike","Bajaj","Red")

print("Type: "+ bike1.type+" Brand: "+bike1.brand+" Color: "+bike1.color)