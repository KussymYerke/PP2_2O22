x = input().split()
ans = []
for i in x:
	res = ''
	for j in i:
		if j.isalpha():
			res += j
	ans.append(res)

ans = list(set(ans))
ans.sort()

print(len(ans))

for i in ans:
	print(i)