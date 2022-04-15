def func(n):
  for i in range(n + 1):
    if(i % 2 == 0):
        yield i

n=int(input())

for i in func(n):
  print(i, end=" ")