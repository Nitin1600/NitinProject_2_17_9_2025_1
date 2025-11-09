# class CustomError(Exception):
#     pass
#
# raise CustomError
# __main__.CustomError
#
# raise CustomError("An error occured")
# __main__.CustomError:An error occured

# class Error(Exception):
#     pass
#
# class ValueTooSmallError(Error):
#     pass
#
# class ValueTooLargeError(Error):
#     pass
#
# number=10
#
# while True:
#     try:
#         i_num = int(input("Guess the number:"))
#         if i_num < number:
#             raise ValueTooSmallError
#         elif i_num > number:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#         print("Oops! Number is too small")
#         print()
#     except ValueTooLargeError:
#         print("Oops! Number is too large")
#         print()
#
# print("Congratulations! You guessed it right")

# class SalaryNotInRangeError(Exception):
#
#     def __init__(self, salary, message="Salary is not in (5000,15000) range"):
#         self.salary=salary
#         self.message=message
#         super().__init__(self.message)
#
# salary=int(input("Enter the salary amount:"))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)

class SalaryNotInRangeError(Exception):

    def __init__(self, salary, message="Salary is not in (5000,15000) range"):
        self.salary=salary
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'

salary=int(input("Enter the salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

