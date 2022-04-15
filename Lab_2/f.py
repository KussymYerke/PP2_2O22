n = int(input())
dic = {}

for i in range(n):
    stud, num = input().split()
    if stud in dic:
        dic[stud] += int(num)
    else:
        dic[stud] = int(num)

k = dic.keys()
m = max(dic.values())
k = list(k)
k.sort()
for i in k:
    if (dic[i] == m):
        print(i, ' is lucky!')
    else:
        print(i, 'has to receive', m - dic[i], 'tenge')