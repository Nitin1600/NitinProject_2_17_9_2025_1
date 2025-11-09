# parameter = "Pramoda"
#
# match parameter:
#     case "Pramod":
#         print("Hi")
#     case "PramOD":
#         print("Hello")
#     case _:
#         print("Default")

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

# import time
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time=time.time()
#         result=func(*args, **kwargs)
#         end_time=time.time()
#         print(f"Function {func.__name__} took {end_time - start_time} to finish")
#         return result
#     return wrapper
#
# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("Function finished")
#
# slow_function()

# class My_class:
#     @staticmethod
#     def static_method():
#         print("This is a static method")
# My_class.static_method()

# class MyClass:
#     class_variable="Hello"
#
#     @classmethod
#     def class_method(cls):
#         print(f"Class Variable Value:{cls.class_variable}")
#
# MyClass.class_method()

# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     @property
#     def value(self):
#         return self._value
#
#     @value.setter
#     def value(self, new_value):
#         self._value=new_value
#
# obj =MyClass(10)
# print(obj.value)
# obj.value=20
# print(obj.value)


# import functools
#
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Before the function call")
#         result=func(*args, **kwargs)
#         print("After the function call")
#         return result
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello")
#
# say_hello()

# class MyClass:
#     @staticmethod
#     def static_method():
#         print("This is a static method")
#
#     @classmethod
#     def class_method(cls):
#         print(f"This is a class method{cls}")
#
#     @property
#     def name(self):
#         return "MyClass"
#
# obj = MyClass()
# obj.static_method()
# obj.class_method()
# print(obj.name)

# def decorator1(func):
#     def wrapper():
#         print("Decorator1")
#         func()
#     return wrapper
#
# def decorator2(func):
#     def wrapper():
#         print("Decorator2")
#         func()
#     return wrapper
#
# @decorator1
# @decorator2
# def say_hello():
#     print("Hello")
#
# say_hello()

import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result=func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a,b):
    return a + b

add(2,3)