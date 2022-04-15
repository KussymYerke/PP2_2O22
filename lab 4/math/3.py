import math
from math import tan
from math import pi

sides = int(input(" #sides: "))
length = float(input(" length of a side: "))
area = sides * (length ** 2) / (4 * tan(pi / sides))

print(round(area))
