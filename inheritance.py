class Shape:
    def __init__(self):
     self.area = 0
     self.colour = "blue"

class Triangle(Shape):
    def tri_area(self, b, h):
        self.area = 0.5*b*h
        return self.area

class Rectangle(Shape):
    def rec_area(self, l, b):
        self.area = l*b
        return self.area

tri1 = Triangle()
print(tri1.tri_area(4, 10), tri1.colour)

rec1 = Rectangle()
print(rec1.rec_area(4, 10), rec1.colour)


    



