x = input()
listi = []
for i in x:
	if (len(listi) == 0):
		listi.append(i)
	elif (i == '(' or i == '{' or i == '['):
		listi.append(i)
	else:
		if (i == ')' and listi[-1] == '(') or (i == ']' and listi[-1] == '[') or (i == '}' and listi[-1] == '{'):
			listi.pop()
		else:
			listi.append(i)

if (len(listi) == 0):
	print('Yes')
else:
	print('No')
#print(ls)