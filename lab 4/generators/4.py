def squares(a,b):

  for i in range(a, b+1, 1):
    yield i ** 2

a, b = list(map( int, input().split()))

for i in squares(a, b):
  print(i, end = " ")

