class Employee(object):
	"""
	This class represents an Employees.

	This class has attributes name, start date(year) and salary.
	However, they are only accessible via thhne getter and setters only.
	"""

	### Hidden attibutes.
	# Attribute _name: It is the name of instance.
	# Invariant :It must be an string.

	# Attribute _startDate: It is a date(year) when employee join.
	# Invariant: it must be int and grater than 1970.

	# Attribute _salary: It is a annual salary of employee.
	# Invariant: It must be int or float and grater than 0.
	def getName(self):
		"""
		Return: The name of Employee.
		The name is non-empty string.
		"""
		return self._name

	def setName(self, value):
		"""
		Sets the employee's name to the given value.

		Parameter value: This is name which you have to enter in employee instance.
		Precondition: It must be an string.
		"""
		assert type(value) == str, str(value) + 'is not a string.'

		self._name = value

	def getDate(self):
		"""
		Return: The date(year) when employee join the company.
		"""
		return self._startDate

	def setDate(self, value = -1):
		"""
		Sets the employee's joining date(year) to the given value.

		you have to specify the year which is greater than 1970 , 
		if you not specified then by default is -1.

		Parameter value: This is date(year) which you have to enter in employee instance.
		Precondition: It must be int and greater than 1970.
		"""
		assert type(value) == int, str(value) + 'is not an int.'
		assert value > 1970 or value == -1, str(value) + 'is not greater than 1970.'

		self._startDate = value

	def getSalary(self):
		"""
		Return: The salary from Employee object.

		Parameter self: It is an object.
		Precondition: It must be an non-empty object.
		"""
		return self._salary

	def setSalary(self, value = 50000):
		"""
		Sets the employee's salary to the given value.

		Default salary of employee instance is 50,000.

		Parameter self: It is an object.
		Precondition: It must be an non-empty object.

		Parameter value: This is salary which you have to enter in employee instance.
		Precondition: It must int or float which greater than 0. 
		"""
		assert type(value) in [int, float], str(value) + ' is not int or float.'
		assert value >= 0, str(value) + ' is not grater than 0 '

		self._salary = value


	def __init__(self, name, date = -1, salary = 50000):
		"""
		This initiates the atributes.
		"""
		# assert type(name) == str and len(name) > 0
		# assert type(date) == int and (date > 1970 or date == -1) 
		# assert type(salary) in [int, float] and salary >= 0

		# self._name = name 
		# self._startDate = date 
		# self._salary = salary

		self.setName(name)
		self.setDate(date)
		self.setSalary(salary)

	def __str__(self):
		"""
		Return: The string representation of class.
		"""
		return 'Name: '+ str(self._name) + ', Joining Date: ' + str(self._startDate) + ', Salary: ' + str(self._salary)

	def __repr__(self):
		"""
		Returns: The string representation of class.
		"""
		return str(self.__class__) + ' ' + str(self)


	def getCompensation(self):
		"""
		Returns: the annual compensation of employee.

		Parameter self: It is an object.
		Precondition: self must be an object.
		"""
		return self._salary

x = Employee('Kirtan', 2023, 50000000000)
# print(repr(x))
# print(x.getCompensation())
# print(x.getName())


# y = Employee('Kirtan', 2023, 500000)




class Executive(Employee):
	"""
	This represent's the Executive employee.
	"""
	### Hidden attribute.
	# Attribute _bonus: it is a bonus attribute.
	# Invarient: It must be int or float.

	def getBonus(self):
		"""
		Return: the bonus of Executive employee.
		"""
		return self._bonus

	def setBonus(self, value = 0.0):
		"""
		Sets the employee's bonus to the given value.

		Default salary of employee instance is 0.0.

		Parameter value: This is bonus which you have to set.
		Precondition: It must int or float which greater than equal 0. 
		"""
		self._bonus = value

	def __init__(self, name, date, salary = 50000, bonus = 0.0):
		super().__init__(name, date, salary)
		self.setBonus(bonus)
		# self._object = o 

	def getCompensation(self):
		return self.getBonus() + self.getSalary()

	def __str__(self):
		return super().__str__() + ', Bonus: ' + str(self._bonus)


y = Executive('Kirtan', 2022, 5000)
print(y.getBonus())
y.setBonus(500)
print(y.getCompensation())
print(y)
# a = Employee('Kirtan', 2023, 500000)

z = Executive('Kirtan', 2023, 20000)

print((z.getBonus(), z.getSalary()))
print(z)

print(isinstance(x, Executive))
print(isinstance(y._name, Executive))
print(y.__dict__)