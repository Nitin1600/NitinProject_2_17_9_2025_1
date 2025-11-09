# class Student:
#     pass
# obj1 = Student()
# obj2 = Student()

# class Pen:
#     pass

# class Pen:
#     def __init__(self,name,colour):
#         self.name = name
#         self.colour = colour
#
# obj=Pen("Reynolds","Blue")
# # print(obj)

# class Pen:
#     def __init__(self,name,colour):
#         self.name=name
#         self.colour=colour
#
#     def printDetails(self):
#         print(self.name, self.colour)
#
# obj1 = Pen("Reynolds", "Blue")
# obj2 = Pen("Cello", "Red")
# obj1.printDetails()
# obj2.printDetails()

class FaceBook:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def login(self):
        print(self.username, "loggedin successfully")

    def logout(self):
        print(self.username, "loggedout successfully")

obj = FaceBook("Raj", "abc000")
obj.login()
obj.logout()
