class Length(object):

	@property
	def lent(self):
		return self._lent

	@lent.setter
	def lent(self, value):
		self._lent = value

	def __init__(self, value):

		self.lent = value

	def __str__(self):
		return str(self.lent) 

class Breadth(object):

	@property
	def bread(self):
		return self._bread

	@bread.setter
	def bread(self, value):
		self._bread = value

	def __init__(self, value):
		self.bread = value

	def __str__(self):
		return str(self.bread)


class Rect_area(Length, Breadth):

	def __init__(self, l, b):
		Breadth.__init__(self, l)
		Length.__init__(self, b)

	def r_area(self):
		return str(int(self.bread) * int(self.lent))

	def __str__(self):
		return str(int(self.bread) * int(self.lent))

x = Rect_area(5, 5)
print(x)
# print(str(x))

	