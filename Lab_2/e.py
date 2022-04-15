"""
arr[i] = x + 2 * i
cin
n and x
"""
listi = input().split()
if (len(listi) == 2  ):
	n, x = listi
else:
	n = listi[0]
	x = input()

x = int(x)
n = int(n)

arr = []
count = 0

for i in range(n):
    arr.append(x + 2 * i)

i = 0

while (i != (len(arr))):
    count = count ^ arr[i]
    i = i + 1

print(count)
