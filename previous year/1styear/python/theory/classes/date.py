class Date(object):
	
	MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	Days = {'Jan' : 31, 'Feb' : 28, 'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31}

	@property
	def year(self):
		'Return: the year of this Date.'
		# assert type(self._year) == int and self._year >= 2000
		return self._year

	@property
	def month(self):
		'Return: the month of this Date.'
		# assert self._month in Date.MONTHS, repr(self._month) + ' is not valid code.'
		return self._month

	@property
	def day(self):
		'Return: the day of this Date.'
		# assert type(self._day) == int and self._day <= Date.Days[self._month]  
		return self._day

	@day.setter
	def day(self, value):
		'''
		Sets the day of this date.

		Parameter value: The new day.
		Precondition: Value is a valid day in the month.
		'''
		assert type(value) == int and value <= Date.Days[self._month], str(value) + ' is not valid day'
		if isleapyear(self.year) == 
		self._day = value



	def __init__(self, y, m, d):
		# assert type(self._day) == int and self._day <= Date.Days[self._month]
		assert m in Date.MONTHS, repr(m) + ' is not valid code.'
		assert type(y) == int and y >= 2000
		assert isleapyear(y)


		self._year = y 
		self._month = m
		self.day = d


	def __str__(self):
		return str(self._month) + ' ' + str(self._day) + ', ' + str(self._year)


	def __lt__(self, other):
		# x = True
		# if self.year < other.year :
		# 	if self.month < other.month :
		# 		if self.day < other.day :
		# 			x = True

		# 		else:
		# 			x = False

		# 	else:
		# 		x = False

		# else:
		# 	x = False

		# return x
		return self._year <= other._year and Date.MONTHS.index(self._month) <= Date.MONTHS.index(other._month) and self._day <= other._day 


a = Date(2044, 'Oct', 5)
b = Date(2054, 'Feb', 8)
a.day
# print(5)

# print(a < b)
print(b.day)
print(str(a))







	
	
	