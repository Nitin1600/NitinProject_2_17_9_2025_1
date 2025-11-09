# print(len("learn"))
# print(len([10,20,30]))
from psycopg2.errorcodes import INDICATOR_OVERFLOW


# def add(x,y,z=0):
#     return x+y+z
#
# print(add(2,3))
# print(add(2,3,4))
# print(add())

# class India():
#     def capital(self):
#         print("New_Delhi is the capital of India")
#
#     def language(self):
#         print("Hindhi is widely spoken language")
#
#     def type(self):
#         print("India is a developing country")
#
# class USA():
#     def capital(self):
#         print("New_York is the capital of USA")
#
#     def language(self):
#         print("English is the primary language")
#
#     def type(self):
#         print("USA is a developed country")
#
# obj_india = India()
# obj_usa = USA()
# for country in (obj_india,obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#
#     def flight(self):
#         print("Most of them can fly, but few cannot")
#
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly")
#
# class Ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly")
#
# obj_bird=Bird()
# obj_sparrow = Sparrow()
# obj_ostrich = Ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_sparrow.intro()
# obj_sparrow.flight()
#
# obj_ostrich.intro()
# obj_ostrich.flight()

# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
# obj_india = India()
# obj_usa = USA()
#
# func(obj_inida)
# func(obj.usa)

# class India():
#
#     def capital(self):
#         print("New_Delhi is the capital of country")
#
#     def language(self):
#         print("Hindhi is widely spoken language")
#
#     def type(self):
#         print("India is a devoloping country")
#
# class USA():
#
#     def capital(self):
#         print("Washington D.C is the capital of USA")
#
#     def language(self):
#         print("English is primary language")
#
#     def type(self):
#         print("USA is a devoloped country")
#
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
# obj_india = India()
# obj_usa = USA()
#
# func(obj_india)
# func(obj_usa)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())