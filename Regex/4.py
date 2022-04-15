import re

def func(s):
	b = '[A-Z][a-z]'
	if re.search(b, s):
		return 'Yes, there is a match'
	else:
		return 'No, there is no match'

s = input()
print(func(s))