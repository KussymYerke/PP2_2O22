n = int(input())

res = []
for j in range(n):

    ans = 0
    ans2 = 0
    ans3 = 0

    s = input()
    for i in s:

        if (i >= 'A' and i <= 'Z'): ans = ans + 1
        elif (i >= 'a' and i <= 'z'): ans2 = ans2 + 1
        elif (i >= '1' and i <= '9'): ans3 = ans3 + 1

    if( ans != 0 and ans2 != 0 and ans3 != 0):
        res.append(s)

res = list(set(res))
res.sort()
print(len(res))
for i in res:
    print(i)