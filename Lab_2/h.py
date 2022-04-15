x, y = map(int, input().split())
n = int(input())
listi = []
for i in range(n):
    x2, y2 = map(int, input().split())
    dist = ((x - x2) ** 2 + (y - y2) ** 2) ** (1 / 2)
    listi.append((dist, x2, y2))
    listi.sort()

for i in listi:
    dist, x2, y2 = i

    print(x2, y2)
