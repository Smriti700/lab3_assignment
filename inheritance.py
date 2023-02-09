class Shape:
    def __init__(self):
     self.area = 0
     self.colour = ""

class Triangle(Shape):
    def tri_area(self, b, h):
        self.area = 0.5*b*h
        return self.area;
    



