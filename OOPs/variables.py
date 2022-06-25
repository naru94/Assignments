class Variables:
    def __init__(self, x, y, z, k):
        self.__x = x
        self.__y = y
        self.__z = z
        self.k_ = k

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y
    def set_z(self, z):
        self.__z = z

    def sqaure_sum(self):
        a = self.__x * self.__x
        b = self.__y * self.__y
        c = self.__z * self.__z

        return a + b + c


obj1 = Variables(1, 2, 3, 4)

print("Value of x: ", obj1.get_x())
print("Value of y: ", obj1.get_y())
print("Value of z: ", obj1.get_z())
print("Value of k: ", obj1.k_)

print("")

obj1.set_x(5)
obj1.set_y(6)
obj1.set_z(7)
obj1.k_ = 8

print("Value of x: ", obj1.get_x())
print("Value of y: ", obj1.get_y())
print("Value of z: ", obj1.get_z())
print("Value of k: ", obj1.k_)

print("Sum of squares: ", obj1.sqaure_sum())
