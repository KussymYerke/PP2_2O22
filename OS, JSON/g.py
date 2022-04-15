f=open("paste.txt", "r")
g=open("copy.txt", "a")
for i in f:
    g.write(i)
g=open("copy.txt", "r")
print(g.read())