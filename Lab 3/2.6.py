def func(n):
    rev = n.split()
    out = rev[::-1]
    for i in out:
        print(i, end=" ")



n = input()
func(n)