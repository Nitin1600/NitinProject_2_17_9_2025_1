# f = open("test1.txt", 'w', encoding="cp1252")
# f.write("this is write operation\n")
# f.write("this is second write operation\n")
# f.close()

# f = open("test1.txt", "r")
# print(f.read())
# f.close()

# try:
#     f = open("test1.txt", "r", encoding="cp1252")
#     print(f.read())
# finally:
#     f.close()

# with open("test1.txt", "r") as f:
#     print(f.read())

# with open("test1.txt", "a") as f:
#     f.write("this is with operation\n")
#     f.write("this is with second operation\n")
#     f.write("this is with third operation\n")
#     f.close()
#
# with open("test1.txt", "r") as f:
#     print(f.tell())
#     print(f.seek(10))
#     print(f.read())
#     f.close()

# with open("test1.txt", "r") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.read(10))
#     print(f.tell())
#     f.close()

# with open("test1.txt", "r") as f:
#     print("1st line is->", f.readline())
#     print("2nd line is->", f.readline())
#     print("3rd line is->", f.readline())
#     print("4th line is->", f.readline())
#     f.close()

# with open("test1.txt", "x") as f:
#     f.write("This is my test exclusive creation")
#     f.close()

# try:
#     with open("test1.txt", "x") as f:
#         f.write("This is my test exclusive creation")
#         f.close()
# except FileExistsError:
#     print("File already exists")