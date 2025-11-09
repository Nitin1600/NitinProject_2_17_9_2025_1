# class Animal:
#     def speak(self):
#         print("Animal speaks!")
#
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#
# dog=Dog()
# dog.speak()
# dog.bark()

# class A:
#     def method_a(self):
#         print("Method_A")
#
# class B:
#     def method_b(self):
#         print("Method_B")
#
# class C(A,B):
#     def method_c(self):
#         print("Method_C")
#
# my_object = C()
# my_object.method_a()
# my_object.method_b()
# my_object.method_c()

# class A:
#     def greet(self):
#         print("Hello from class A")
#
# class B:
#     def greet(self):
#         print("Hello from class B")
#
# class C(A,B):
#     pass
#
# class D(B,A):
#     pass
#
# obj1 = A()
# obj1.greet()
#
# obj2=B()
# obj2.greet()
#
# print(C.mro())
# print(D.mro())

# class Vehicle:
#     def start_engine(self):
#         print("Engine started")
#
# class Car(Vehicle):
#     def drive(self):
#         print("Driving the car")
#
# class SportsCar(Car):
#     def race(self):
#         print("Racing the sports car")
#
# obj=SportsCar()
# obj.start_engine()
# obj.drive()
# obj.race()

# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
#
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")
#
# dog=Dog()
# dog.speak()
# dog.bark()
#
# cat = Cat()
# cat.speak()
# cat.meow()

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

rect = Rectangle(2,3)
print(rect.area())
print(rect.perimeter())

circle = Circle(4)
print(circle.area())
print(circle.perimeter())
