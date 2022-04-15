a = int(input())
b = input()

if ( b == 'k'):
    c = input()
    d = "{:." + c + "f}"
    print(d.format(a/1024))

else:
    print(a * 1024)

