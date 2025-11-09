# f = open("open.txt")
# f = open("C:/Python38/README.txt")

# f = open("test.txt")
# f = open("test.txt", 'w')
# f = open("img.bmp", 'r+b')

# f = open("test.txt", mode="r", encoding="utf-8")

# f = open("test.txt", encoding="utf-8")
# f.close()
# f = open("C:/Users/nitingpa/hello.txt")

# try:
#     f = open("test.txt", encoding="utf-8")
# finally:
#     f.close()

# with open("test.txt", encoding="utf-8") as f:

# with open("test.txt", 'w', encoding="utf-8") as f:
#     f.write("My first file\n")
#     f.write("This file\n\n")
#     f.write("contains three lines\n")
#
# f = open("test.txt", "r", encoding="utf-8")
# print(f.read(4))
# print(f.read(4))
# print(f.read())
# print(f.tell())
# print(f.seek(0))
# print(f.read())

# for line in f:
#     print(line, end='')

f = open("test.txt", 'r', encoding="utf-8")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines())