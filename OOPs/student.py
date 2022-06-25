class Student:
    def __init__(self, name, phy, chm, bio, math):
        self.__name = name
        self.__phy = phy
        self.__chm = chm
        self.__bio = bio
        self.__math = math

    def get_name(self):
        return self.__name

    def get_phy(self):
        return self.__phy

    def get_chm(self):
        return self.__chm

    def get_bio(self):
        return self.__bio

    def get_math(self):
        return self.__math

    def set_name(self, name):
        self.__name = name

    def set_phy(self, phy):
        self.__phy = phy

    def set_chm(self, chm):
        self.__chm = chm

    def set_bio(self, bio):
        self.__bio = bio

    def set_math(self, math):
        self.__math = math

    def totalObtained(self):
        return self.__phy + self.__chm + self.__bio + self.__math

    def calPercentage(self):
        return (self.totalObtained() / 400 * 100)

Dravid = Student("Rahul Dravid", None, None, None, None)
Sachin = Student("Sachin Tendulkar", 98, 92, 90, 100)

Dravid.set_phy(int(input("Enter Physics marks: ")))
Dravid.set_chm(int(input("Enter Chemistry marks: ")))
Dravid.set_bio(int(input("Enter Biology marks: ")))
Dravid.set_math(int(input("Enter Mathematics marks: ")))

print("Name of the Student: ", Sachin.get_name())
print("Physics: ", Sachin.get_phy())
print("Chemistry: ", Sachin.get_chm())
print("Biology: ", Sachin.get_bio())
print("Mathematics: ", Sachin.get_math())

print("Total Marks: ", Sachin.totalObtained())
print("Percentage: ", Sachin.calPercentage())

print("Name of the Student: ", Dravid.get_name())
print("Physics: ", Dravid.get_phy())
print("Chemistry: ", Dravid.get_chm())
print("Biology: ", Dravid.get_bio())
print("Mathematics: ", Dravid.get_math())

print("Total Marks: ", Dravid.totalObtained())
print("Percentage: ", Dravid.calPercentage())