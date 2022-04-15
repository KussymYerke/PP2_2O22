n = int(input())
for r in range(1, n+1):
        for c in range(1, n + 1):
            if(r == 1 or c == 1):
                print( (r * c) - 1, end=" ")

            elif( (r != 1 and c != 1) and r == c):
                print( ((r - 1)*(c - 1)), end=" ")

            else:
                print(0, end=" ")
        print()
