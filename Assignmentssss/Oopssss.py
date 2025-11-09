# class Animal:
#     category = "animal"
#
#     def __init__(self,name,colour,speciality):
#         self.name=name
#         self.colour=colour
#         self.speciality=speciality
#
#     def printDetails(self):
#         a=20
#         b=10
#         print(self.category)
#         print(self.name,self.colour,self.speciality)
#
# obj1 = Animal("Lion", "Yellow", "King")
# obj2= Animal("Tiger", "Orange", "Stunning")
# obj1.printDetails()
# obj2.printDetails()
# obj1.category="ttt"

class Vehicle:
    category="Bike"

    def __init__(self,name,colour,brand):
        self.name=name
        self.colour=colour
        self.brand=brand

    def printDetails(self):
        print(self.category)
        print(self.brand,self.name,self.colour)

obj1=Vehicle("N_S_200", "White", "Pulsar")
obj2 =Vehicle("Splendor_Plus", "Black", "Hero")
obj1.printDetails()
obj2.printDetails()
obj1.category="ttt"