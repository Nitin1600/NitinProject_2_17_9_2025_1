# (1)

# table = int(input("Enter the table:"))
#
# print(f"{table}*1={table*1}")
# print(f"{table}*2={table*2}")
# print(f"{table}*3={table*3}")
# print(f"{table}*4={table*4}")
# print(f"{table}*5={table*5}")
# print(f"{table}*6={table*6}")
# print(f"{table}*7={table*7}")
# print(f"{table}*8={table*8}")
# print(f"{table}*9={table*9}")
# print(f"{table}*10={table*10}")

# (2)

# num1 = int(input("Enter the numner1:"))
# num2 = int(input("Enter the number2:"))
#
# max_num = max(num1, num2)
# print(f"Maximum number is: {max_num}")
#
# Sum = num1 + num2
# print("Sum is", f"{Sum}")
#
# Sub = num1 - num2
# print(f"Sub is: {Sub}")
#
# Mul = num1*num2
# print(f"Mul is:{Mul}")
#
# Div = num1 / num2
# print(f"Div is:{Div}")
#
# Pow = num1**num2
# print(f"Pow is:{Pow}")
#
# Whole = num1 // num2
# print(f"Whole: {Whole}")

#(3)Theoretical

#(4)
# pi=3.14
# radius=float(input("Enter the radius of the circle:"))
# area = pi * radius ** 2
# print(f"Area of the circle with radius {radius} is {area}")

# (5)
# num1 = float(input("Enter the number1:"))
# num2 = float(input("Enter the number2:"))
#
# if num1 > num2:
#     print(f"{num1} is greater then {num2}")
# elif num1 < num2:
#     print(f"{num1} is lesser then {num2}")
# else:
#     print(f"{num1} and {num2} are equal")

# (6)
# num = int(input("Enter the number:"))
# # num2 = int(input("Enter the number2:"))
#
# Square = num ** 2
# Cube = num ** 3
#
# print(f"Square of {num} is {Square}")
# print(f"Cube of {num} is {Cube}")

# (7)

# Year = int(input("Enter the Year:"))
# if (Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0):
#     print(f"{Year} is a leap year")
# else:
#     print(f"{Year} is not a leap year")

# (8)

# a = float(input("Enter the first side of the triangle:\n"))
# b = float(input("Enter the second side of the triangle:\n"))
# c = float(input("Enter the third side of the triangle:\n"))
#
# if a==b and a==c and b==c:
#     print("triangle is equilateral")
# elif a==b!=c or a==c!=b or b==c!=a:
#     print("triangle is isosceles")
# else:
#     print("Triangle is scalene")

# (9)

# FizzBuzz

# for i in range(1,101,1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# (10.a)
# num = int(input("Enter the number to find factorial of:\n"))
# fact=1
# i=num
# while i >= 1:
#     fact=i*fact
#     i=i-1
# print(f"Factorial of {num} is {fact}")

# (10.b)
# num = int(input("Enter the number to find factorial of:\n"))
# res=1
# if num == 0:
#     print(1)
# else:
#     for i in range(1, num+1):
#         res=i*res
# print(f"Factorial of {num} is {res}")

# (11)

n = int(input("Enter the number:"))
f1=0
f2=1
sum=0
if n <= 0:
    print("Please enter the positive number")
elif n == 1:
    print(f1)
else:
    # print("ENter first two numbers")
    # print(f1, f2, end=" ")
    for i in range(n):
        sum=f1+f2
        print(sum, end=" ")
        f1=f2
        f2=sum
    # print(sum, end="")

# f = int(input("Enter the number:"))
# a=0
# b=1
# fib=0
# if f == 0:
#     print(0)
# elif f == 1:
#     print(0)
# else:
#     for i in range(0, f+2):
#         fib=a+b
#         a=b
#         b=fib
#         print(fib, end=" ")