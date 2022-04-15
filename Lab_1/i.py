liist = []

a = int(input())

for x in range(0, a):
    element = str(input())
    if ( element.find("@gmail.com") != -1): # if they can't find it then it will equal to negative one
        liist.append(element)

for x in liist:
    print(x[0:len(x)-10])