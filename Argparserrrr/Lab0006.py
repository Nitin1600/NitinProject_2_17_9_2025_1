# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("num1", help="first_number")
# parser.add_argument("num2", help="second_number")
# parser.add_argument("operation", help="operation")
#
# args=parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
#
# n1 = int(args.num1)
# n2 = int(args.num2)
#
# result = n1+n2
# print("The result is: ", result)

# import argparse
#
# parser=argparse.ArgumentParser()
# parser.add_argument("num1", help="first_number")
# parser.add_argument("num2", help="second_number")
# parser.add_argument("operation", help="operation")
#
# args=parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
#
# n1=int(args.num1)
# n2=int(args.num2)
#
# if args.operation == "add":
#     result=n1+n2
#
# elif args.operation == "sub":
#     result=n1-n2
#
# elif args.operation == "mul":
#     result=n1*n2
#
# elif args.operation == "div":
#     result=n1/n2
#
# else:
#     print("Unmatched argument")
#
# print("The result is: ", result)

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("num", help="Enter number to get square of it")
# args=parser.parse_args()
# print(args.num ** 2)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num", help="Enter the number to get square of it", type=int)
args=parser.parse_args()
print(args.num ** 2)

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("--num1", help="first_number")
# parser.add_argument("--num2", help="second_number")
# parser.add_argument("--operation", help="operation")
#
# args=parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
#
# n1=int(args.num1)
# n2=int(args.num2)
#
# if args.operation=="add":
#     result=n1+n2
#
# elif args.opertion=="sub":
#     result=n1-n2
#
# elif args.operation=="mul":
#     result=n1*n2
#
# elif args.operation=="div":
#     result=n1/n2
#
# else:
#     print("Unmatched argument")
#
# print("The result is: ", result)

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("example")
# args=parser.parse_args()
# print(args.example)
#
# if args.example=="Hello Python":
#     print("Welcome to LearnMore")
#
# else:
#     print("Unmatched Argument")

# import argparse
#
# parser=argparse.ArgumentParser()
# parser.add_argument("example", default="Hello How are you")
# args=parser.parse_args()
# # print(args.example)
#
# if args.example=="Hello":
#     print("Welcome to LearnMore")
#
# else:
#     print("Didn't make it")

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-tut", "--tutorial", help="Best Tutorial")
# parser.add_argument("-w", "--writer", help="Technical Content")
# args=parser.parse_args()
#
# if args.tutorial=="LearnMore":
#     print("Congratulations | You made it")
#
# if args.writer=="Devansh":
#     print("Technical Writer")

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("tutorial", help="Best Tutorial")
# parser.add_argument("-w", "--writer", help="Technical Content")
# args=parser.parse_args()
#
# if args.tutorial=="LearnMore":
#     print("You made it!")
#
# if args.writer=="Devansh":
#     print("Technical writer")