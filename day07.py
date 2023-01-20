class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다.')

class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        import math
        return self.width * self.length

    def __repr__(self):  #magic method
        return f'사각형의 좌표는 x: {self.x}, y: {self.y}이고 넓이는 {self.get_area()}입니다.'

    def __add__(self, other):
        # 넓이의 단순 합
        # return self.get_area() + other.get_area()
        # 각각의 사각형의 밑변과 높이를 더해 만든 사각형의 넓이
        return Rectangle(0, 0, self.width + other.width, self.length+other.length)
r1 = Rectangle(100,50, 5,2)
print(r1)

r2 = Rectangle(100,100,10,5)
print(r2)