def func(n):
  while(n):
    yield n
    n -= 1

n=int(input())

for i in func(n):
  print(i, end=" ")

print(0)