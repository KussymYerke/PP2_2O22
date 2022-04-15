import re

def func(s):
	ls = re.findall('[A-Z][a-z]*', x)

	return ' '.join(ls)

s = input()
print(func(s))