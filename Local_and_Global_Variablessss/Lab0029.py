# a = 5
# def abc():
#     b = 10
#     print(b)
# print(a)
# abc()

# a=5
# def sum():
#     print(a)
#
# print(a)
# sum()

# a=5
# def sum():
#     a=a+2
#     print(a)
#
# print(a)
# sum()

# a=5
# def sum():
#     global a
#     a = a+2
#     # print(a)
#
# print(a)
# sum()
# print(a)

# def foo():
#     x=20
#     def bar():
#         global x
#         x=25
#         # print(x)
#     print("Before calling bar:", x)
#     print("Calling bar now")
#     bar()
#     print("After calling bar:", x)
# # (x)
# foo()
# print("x in main:", x)

# def A():
#     print("How are you")
#     def B():
#         print("Hello world")
#     print("Nested function is executing")
#     B()
#
# A()

# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         # print("inner:", x)
#     print(x)
#     inner()
#     print(x)
#     print("a", x)
#
# outer()
# print(x)

# def addtwonumber(a,b):
#     # a=10
#     # b=5
#     c=a+b
#     print(c)
#
# addtwonumber(2,3)

# def oddoreven(num):
#     # num=4
#     if num%2==0:
#         print(num, "is even number")
#     else:
#         print(num, "is odd number")
#
# oddoreven(6)