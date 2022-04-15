def func(h, l):
    rabbit = (l - 2 * h) / 2
    chicken = h - rabbit
    print(int(rabbit))
    print(int(chicken))

h = int(input())
l = int(input())

func(h, l)