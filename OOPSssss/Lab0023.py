# class Base:
#     d = 10
#     def __init__(self):
#         self._a = 2
#         self.b = 5
#
# obj = Base()
# print(obj._a)
# print(obj.b)
# print(obj.d)

# class Base:
#     def __init__(self):
#         self.__a=2
#         self.b=5
#
# obj=Base()
# print(obj._Base__a)
# print(obj.b)

# class Base:
#     def __init__(self):
#         self.a ="Geeks_for_Geeks"
#         self.__b="Hellonfire"
#         self._c="Hyper"
#
#     def _Pen(self):
#         self.d = "Hyperism"
#         return self.d
#
#     def __Pencil(self):
#         self.e = "Clan"
#         return self.e
#
#     def Eraser(self):
#         self.f = "Game"
#         return self.f
#
# obj = Base()
# print(obj.a)
# print(obj._c)
# # print(obj.__b)
# print(obj._Base__b)
# print(obj._Pen())
# print(obj._Base__Pencil())
# print(obj.Eraser())


class Stationary:
    def _pen(self):
        self.d="Hyper"
        return self.d

    def __abcd(self):
        self.z = "z"
        return self.z

class Main(Stationary):
    def __pencil(self):
        self.e="Clan"
        return self.e

    def eraser(self):
        self.f = "Game"
        return self.f

obj=Main()
print(obj._pen())
print(obj._Main__pencil())
print(obj.eraser())
# print(obj._Main__abcd())
print(obj._Stationary__abcd())