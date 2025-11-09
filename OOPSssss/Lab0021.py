# class Student:
#     pass
#
# obj1 = Student()
# obj2 = Student()

# class Pen:
#     pass

# class Pen:
#
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#
# obj = Pen("Reynolds", "Blue")

# class Pen:
#
#     def __init__(self, name,colour):
#         self.name = name
#         self.colour = colour
#
#     def PrintDetails(self):
#         print(self.name, self.colour)
#
# obj1 = Pen("Reynolds", "Blue")
# obj2 = Pen("Cello", "Red")
# obj1.PrintDetails()
# obj2.PrintDetails()

# class FaceBook:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def login(self):
#         print(self.username, "logged in successfully")
#
#     def logout(self):
#         print(self.username, "logged out successfully")
#
# obj = FaceBook("Amith", "abc000")
# obj.login()
# obj.logout()

class Pen:
    material="pen"

    def __init__(self, name,colour,brand):
        self.name=name
        self.colour=colour
        self.brand=brand

    def PrintDetails(self):
        a=10
        b=20
        print(self.material)
        print(self.name, self.colour, self.brand)

obj1 = Pen("Reynolds", "Blue", "Britania")
obj2= Pen("Cello", "Red", "R")
obj1.PrintDetails()
obj2.PrintDetails()
obj1.material="ttt"
obj1.PrintDetails()
