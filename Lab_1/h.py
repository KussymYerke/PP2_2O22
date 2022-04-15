a = str(input())
b = str(input())

c = a.find(b)
d = a[::-1]
e = d.find(b)
f = len(a) - 1 - e
if( f == c):
    print(c)
elif( f != c):
    print( c, '', f)
