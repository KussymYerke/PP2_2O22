a = str(input())
for x in a:
    if ( ord(x) >= 65 and ord(x) <= 90):
        b = ord(x) + 32
        print(chr(b), end='')

    else: print(x, end='')