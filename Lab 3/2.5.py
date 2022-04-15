from itertools import permutations

def func(n):

    for case in permutations(n):
        print(''.join(case))

n = input()
func(n)
