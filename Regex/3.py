import re

def func(s):
	b = '^[a-z]+_[a-z]'
	if re.search(b, s):
		return 'There is a match'
	else:
		return 'No match'

s = input()
print(func(s))