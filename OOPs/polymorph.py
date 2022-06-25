class Shape:
    sname_ = "Shape"

    def getName(self):
        return self.sname_

class ShapeX(Shape):
    def __init__(self, name):
        self.snamex_ = name

    def getName(self):
        return (super().getName() + ": " + self.snamex_)

circle = ShapeX("Circle")
print(circle.getName())

shape = Shape()
print(shape.getName())