# class A:
#     pass
#
# class B(A):
#     pass
from pandas.io.sas.sas_constants import column_type_offset


# class A:
#     pass
#
# class B:
#     pass
#
# class C(A,B):
#     pass

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass

# class Student:
#     def PrintDetails(self):
#         print("Hello, Raj goodmorning")
#
# class Main(Student):
#     pass
#
# obj = Main()
# obj.PrintDetails()

# class Student:
#
#     def PrintDetails(self):
#         print("Hello, Raj goodmorning")
#
# class Address:
#
#     def PrintAddress(self):
#         print("I am from bengaluru")
#
# class Main(Student, Address):
#     pass
#
# obj = Main()
# obj.PrintDetails()
# obj.PrintAddress()

# class Student:
#
#     def PrintDetails(self):
#         print("Hello, Raj goodmorning")
#
# class Address(Student):
#
#     def PrintAddress(self):
#         print("I am from bengaluru")
#
# class Main(Address):
#     pass
#
# obj = Main()
# obj.PrintDetails()
# obj.PrintAddress()

class Student:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def PrintDetails(self):
        print(self.name, self.age)

class Address(Student):

    def __init__(self, name,age,address):
        self.address = address
        Student.__init__(self, name,age)

    def PrintFUllDetails(self):
        print(self.name, self.age, self.address)

class City(Address):

    def __init__(self, name,age, address,city):
        self.city = city
        Address.__init__(self, name,age,address)

    def PrintFullDetails1(self):
        print(self.name, self.age, self.address, self.city)

class Main(City):
    pass

obj = Main("Raj", 12, "Bengaluru", "Karnataka")
obj1 = Main("Vijay", 34, "Chennai", "TamilNadu")
obj1.PrintDetails()
obj.PrintFullDetails1()
obj1.PrintFullDetails1()

