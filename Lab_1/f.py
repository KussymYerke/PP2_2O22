liist = []
a = int(input())
for x in range(0, a):
    listing = int(input())

    liist.append(listing)  # adding the element

for x in liist:
    if(x <= 10):
        print("Go to work!")
    elif(x > 10 and x <= 25):
        print("You are weak")
    elif(x > 25 and x <= 45):
        print("Okay, fine")
    elif(x>45):
        print("Burn! Burn! Burn Young!")

