import re

def func(s):
	y = re.split('_', s)
	return y[0] + ''.join(x.title() for x in y[1:])

s = input()
print(func(s))