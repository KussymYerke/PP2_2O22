n = int(input())
result = []
listi = []

for i in range(n):
    num = input().split()
    if(num[0] == "1"):
        listi.append(num[1])
    elif (num[0] == "2"):
        result.append(listi.pop(0))
for i in result:
	print(i, end = " ")