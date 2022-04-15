def func(n):
    l = ''
    res = []
    for i in n:
        if i == 0:
            pass
        else:
            for j in range(2, int(i/2) + 1):
                if ( i % j == 0):
                    break
            else:
                res.append(i)

    return res

k = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
print(func(k))
