n = int(input())
demon = {}

for i in range(n):
	name, weak = input().split()

	if weak in demon:
		demon[weak] = demon[weak] + 1

	else:
		demon[weak] = 1

m = int(input())

for i in range(m):
	name, power, kill = input().split()
	if power in demon:
		demon[power] = max((demon[power] - int(kill), 0))


k = sum(list(demon.values()))

print('Demons left:', k)

