import re

def func(s):
	b = 'ab*'
	if re.search(b, x):
		return 'There is a match'
	else:
		return 'No match'

s = str(input())
print(func(s))