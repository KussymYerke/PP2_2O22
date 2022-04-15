def func(n):
    check = False

    for i in range(len(n)):
        if(i + 2 == len(n)):
            check = False
            break
        if(n[i] == 0 and n[i+1] == 0 and n[i+2] == 7):
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