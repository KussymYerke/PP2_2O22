import datetime

x = datetime.datetime.now()

print(x.year, end="-")
if(x.month < 10):
    print("0"+str(x.month), end="-")
else:
    print(x.month, end="-")

if(x.day < 10):
    print("0"+str(x.day), end=" ")
else:
    print(x.day, end=" ")

if(x.hour<10):
    print("0" + str(x.hour), end=":")
else:
    print(x.hour, end=":")

if(x.minute<10):
    print("0" + str(x.minute), end=":")
else:
    print(x.minute, end=":")

if(x.second<10):
    print("0" + str(x.second), end="")
else:
    print(x.second, end="")