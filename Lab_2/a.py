liisti = input().split()

maxi = 0
x = len(liisti)
for i in range(x):
	maxi = max(i + int(liisti[i]), maxi)
	if ((maxi < i or maxi == i) and i != len(liisti)-1):
		print(0)
		break
else:
	print(1)
