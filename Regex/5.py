import re

def func(s):
	b = '^a.*b$'
	if re.search(b, s):
		return 'Yes, there is a match'
	else:
		return 'No, there is no match'

s = input()
print(func(s))