def func(n):
    check = False

    for i in range(len(n)):
        if(i + 1 == len(n)):
            check = False
            break
        if(n[i] == 3 and n[i+1] == 3):
            check = True
            break
        else:
            check = False
    if(check):
        print(True)
    else:
        print(False)




n = list(map(int, input().split()))
func(n)