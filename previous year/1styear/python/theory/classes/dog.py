class Dog:
	def __init__(self, name, breed, age, color):
		
		self.name = name
		self.breed = breed
		self.age = age
		self.color = color

	def __str__(self):
		return '(' + str(self.name) + ', ' + str(self.breed) + ', ' + str(self.age) + ', ' + str(self.color) + ')'

	def __repr__(self):
		return str(self.__class__) + ' ' + str(self)


