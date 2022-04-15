class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        #Shape._init_(self)
        self.len = length
    def area(self):
        return self.len ** 2

x = Square(int(input()))
print(x.area())