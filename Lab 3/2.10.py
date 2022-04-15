def func(x):
  d = {}
  lst = []

  for i in x:
    if i not in d:
      lst.append(i)
      d[i] = 1

  for i in d:
    print(i, end = " ")

x = (list(map(int, input().split())))
func(x)
