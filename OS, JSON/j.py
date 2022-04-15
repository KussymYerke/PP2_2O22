n = int(input())

ans = 0
ans2 = 0
ans3 = 0
res = []
for j in range(n):

    s = input()
        for i in range(len(s)):

        if (ord(s[i]) >= 65 or ord(s[i]) <= 90): ans = ans + 1
        elif (ord(s[i]) >= 97 or ord(s[i]) <= 122): ans2 = ans2 + 1
        elif (ord(s[i]) >= 0 or ord(s[i]) <= 9): ans3 = ans3 + 1

    if( ans != 0 and ans2 != 0 and ans3 != 0):
        res.append(s)

res = list(set(res))
res.sort()
print(len(res))
for i in res:
    print(i)