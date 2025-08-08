from Class import Vehicle

class Bike(Vehicle):
    def drive(self):
        print("Drive on two wheels")

#Creating a object
bike1 = Bike("Bike","Bajaj","Red")

print("Type: "+ bike1.type+" Brand: "+bike1.brand+" Color: "+bike1.color)

#this is single inheritance, There are multiple, malilevel, hybrid, hierarchical, inheritance. but some languages do not support multiple inheritance.(like java)