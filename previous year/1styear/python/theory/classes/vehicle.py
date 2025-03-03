class Vehicle:
	"""
	It represents the information(brand, model, type) of vehicle.

	Attribute brand: 
	"""
	def __init__(self, brand, model, type):
		self.brand = brand
		self.model = model
		self.type1 = type1

	def __str__(self):
		return '(' + str(self.brand) + ', ' + str(self.model) + ', ' + str(self.type1) + ')'

	def __repr__(self):
		return str(self.__class__) + ' ' + str(self)

