a = input()
b = sum(ord(x) for x in a) # sum function sums all the numbers, whereas ord() converts letters into numbers
if(b > 300):
    print("It is tasty!")
else: print("Oh, no!")