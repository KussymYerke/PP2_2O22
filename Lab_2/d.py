n = int(input())

if(n % 2 == 0):
    for r in range(1, n+1):
        for c in range(1, n+1):
            if( c == 1):
                print("#", end="")
            elif( (r != 1) and r == c):
                print("#", end="")
            elif( r > c):
                print("#", end="")
            else:
                print(".", end="")

        print()

else:
    for r in range(1, n+1):
        for c in range(1, n+1):
            if( c == n):
                print("#", end="")
            elif( r + c == n + 1):
                print("#", end="")
            elif( r + c > n):
                print("#", end="")
            else:
                print(".", end="")

        print()

