class Person :
	def __init__(self, name, age, gender, aadhar):
		self.name = name
		self.age = age
		self.gender = gender
		self.aadhar = aadhar

	def __str__(self):
		return '(' + str(self.name) + ', ' + str(self.age) + ', ' + str(self.gender) + ', ' + str(self.aadhar) + ')'

	def __repr__(self):
		return str(self.__class__) + ' ' + str(self)
