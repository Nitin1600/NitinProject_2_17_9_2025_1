# f = open("data.txt", "w")
# f.write("This is my first line\n")
# f.write("This is my second line\n")
# f.write("This is my third line")
# f.close()
#
# f = open("data.txt", "r")
# print(f.read())
# f.close()

# f = open("data.txt", "r")
# for line in f:
#     print(line, end="")
# f.close()

# try:
#     f = open("data.txt", "r")
#     print(f.read())
# finally:
#     f.close()

# with open("data.txt", "r", encoding="cp1252") as f:
#     print(f.read())

# with open("data.txt", "r", encoding="cp1252") as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.tell())
#     print(f.seek(0))
#     print(f.read())

# with open("data.txt", "r", encoding="cp1252") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.tell())
#     print(f.seek(0))
#     print(f.readlines())

with open("data.txt", "a", encoding="cp1252") as f:
    f.write("\n This is my fourth line")

with open("data.txt", "x", encoding="cp1252") as f:
    f.write("\n This is my fourth line")


