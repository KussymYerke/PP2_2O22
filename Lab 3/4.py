class Point():
	def __init__(self, first, second):
		self.f = first
		self.s = second
	def show(self):
		print(self.f, self.s)
	def move(self, first, second):
		self.f = first
		self.s = second
	def dist(self, secc):
		return ((self.f - secc.f) ** 2 + (self.s - secc.s) ** 2) ** (1/2)
