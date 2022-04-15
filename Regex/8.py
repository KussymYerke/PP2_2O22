import re

def func(s):
	ls = re.findall('[A-Z][a-z]*', s)
	for i in ls:
		print(i, end=" ")


s = input()
func(s)