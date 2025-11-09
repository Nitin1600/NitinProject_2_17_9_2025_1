# a = 10
# b = 'a'
# try:
#     result = a/int(b)
#     print(result)
# except ZeroDivisionError as e1:
#     print("ZeroDivisionError occured:", e1)
# except TypeError as e2:
#     print("typeError:",e2)
# except ValueError as e3:
#     print("ValueError:",e3)
# except Exception as e4:
#     print("Exception is:",e4)

# try:
#     f=open("test.txt", encoding="cp1252")
#     print(f)
# except FileNotFoundError as f1:
#     print("File details:", f1)

# class InvalidageException(Exception):
#     age=14
#     class License(InvalidageException):
# # age=14
#         if age >= 18:
#             print("Eligible")
#         else:
#             try:
#                 raise InvalidageException("Age is not valid")
#             except InvalidageException as e:
#                 print(e)
