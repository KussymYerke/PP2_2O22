res = []
while(True):
	x = input()
	if (len(x) == 1):
		break

	day, mon, year = x.split()

	res.append((year, mon, day))

res.sort()

for i in res:
	year, mon, day = i
	print(day, mon, year)