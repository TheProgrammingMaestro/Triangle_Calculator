import math
class Triangle:
    def __init__(self, a, b, c, math):
        self.a = a
        self.b = b
        self.c = c
        self.s = ((self.a + self.b + self.c) / 2)
        self.p = (self.a + self.b + self.c)    
        self.area1 = math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
    def __str__(self):
        return "Area: " + str(self.area1) + "\n" + "Perimeter: " + str(self.p)

a = int(input("Enter a side length: "))
b = int(input("Enter a second side length: "))
c = int(input("Enter a third side length: "))
triangle = Triangle(a, b, c, math)
print(triangle)
