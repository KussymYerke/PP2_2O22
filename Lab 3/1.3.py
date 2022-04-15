class Shape():
  def __init__(self):
    pass
  def area(self):
    return 0

class Rectangle(Shape):
  def __init__(self, length, width):
    Shape.__init__(self)
    self.ln = length
    self.wi = width
  def area(self):
    return self.ln * self.wi
a, b = list(map(int, input().split()))
x = Rectangle(a, b)

print(x.area())