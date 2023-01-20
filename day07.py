class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다.')

class Circle(Shape):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius = radius

    def get_area(self):
        import math
        return math.pi * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        import math
        return self.width * self.length

class Triangle(Shape):
    def __init__(self, x, y, base, heigh):
        super().__init__(x, y)
        self.base = base
        self.heigh = heigh

    def get_area(self):
        return (self.base * self.heigh)/2


class Cylinder(Circle):
    def __init__(self, x, y, radius,height):
        super().__init__(x, y,radius)
        self.height = height

    def get_area(self):
        return super().get_area() * self.height

c1 = Circle(100,100, 10)
c2 = Circle(50,50,2.0)
r1 = Rectangle(100,50, 5,2)
c3 = Cylinder(10,10,10,10)
print(c3.get_area())

print(f'사각형의 좌표는 x: {r1.x}, y: {r1.y}이고 넓이는 {r1.get_area()}입니다.')