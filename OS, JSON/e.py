import string
chars=string.ascii_lowercase
f=open("file.txt", "w")
for i in chars:
    f.write(i)
f=open("file.txt", "r")
print(f.read())