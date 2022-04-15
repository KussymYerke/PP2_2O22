class upper():
    def __init__(self):
        self.s = ""
    def getstring(self):
        self.s = input()
    def printstring(self):
        print(self.s.upper())
s = upper()
s.getstring()
s.printstring()
