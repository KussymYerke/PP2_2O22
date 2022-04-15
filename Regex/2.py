import re

def func(s):
	b = 'ab{2,3}?'
	if re.search(b, s):
		return 'There is a match'
	else:
		return 'No match'

s = input()
print(func(s))