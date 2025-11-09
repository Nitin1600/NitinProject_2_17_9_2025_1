# a = 5
# b=0
# result=a/b
# print(result)
# print("hello world")

# a=5
# b=0
# try:
#     result=a/b
#     print(result)
# except ZeroDivisionError as e:
#     print("Error handled:",e)
# print("hello world")

# a=5
# b=0
# try:
#     result=a/b
#     print(result)
# except ZeroDivisionError as e:
#     print("Error handled:",e)
# except TypeError as e1:
#     print("type:",e1)
# print("hello world")

# a=5
# b='a'
# try:
#     result=a/int(b)
#     print(result)
# except ZeroDivisionError as e1:
#     print("Error handled:",e1)
# except TypeError as e2:
#     print("type:",e2)
# except ValueError as e3:
#     print("Value Error:",e3)
# print("hello world")

# import sys
#
# randomList = ['a', 0, 2]
# for entry in randomList:
#     try:
#         print("The entry is:",entry)
#         result=1/int(entry)
#         break
#     except:
#         print("Oops!", sys.exc_info()[0], "occured")
#         print("Next Entry!")
#         print()
# print("Reciprocal of", entry, "is", result)

# try:
#     num = int(input("Entry the even number:"))
#     assert num%2==0
# except:
#     print("Not a even number!")
# else:
#     reciprocal = (1/num)
#     print(reciprocal)
# print("The reciprocal of num is:",reciprocal)

# try:
#     f=open("test.txt", encoding="cp1252")
# finally:
#     f.close()

# class InvalidageException(Exception):
#
#     class License(InvalidageException):
#         age=14
#         if age >= 18:
#             print("Eligible")
#         else:
#             try:
#                 raise InvalidageException("Age is not valid")
#             except InvalidageException as e:
#                 print("e")

    class InvalidageException(Exception):
    class License(InvalidageException):
        age=14
        if age >= 18:
            print("Eligible")
        else:
            try:
                raise InvalidageException("Age is not valid")
            except InvalidageException as e:
                print("e")

