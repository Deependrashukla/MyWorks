class Time(object):
	"""kjhvkjnfvjkn
	"""

	def _is_minute(self, minute):
		return (type(minute) == int and minute >= 0 and minute < 60)

	def __init__(self, hour, minute):
		""" vompuyufu
		"""

		assert 0 <= hour <= 23 , str(hour) + 'is in between [0, 23]'
		assert 0 <= minute <= 59, str(minute) + 'is in between [0, 59]'
		self.hour = hour
		self.minute = minute

	def increment(self, hours, minutes):
		"""
		"""

		assert type(hours) == int 
		assert type(minutes) == int
		assert hours > 0
		assert 0 <= minutes and minutes < 60


		# self.minute += t.minute
		# self.hour += (t.hour + self.minute // 60)
		# self.minute = self.minute % 60
		# self.hour = self.hour % 24


		self.minute += minutes
		self.hour += (hours + self.minute // 60)
		self.minute = self.minute % 60
		self.hour = self.hour % 24


	# def __repr__(self):
		# return str(self.__class__) + ' (' + str(self.hour) + ', ' + str(self.minute) + ')'


	def getHour(self):
		return self.hour


	def setHour(self, value):
		"""
		"""
		assert type(value) == int
		assert 0 <= value < 24

		self.hour = value



x = Time(2, 10)
print(x._is_minute(10))
# x.hour = 'hello'
# print(x)
# print(x.setHour(5))
# print(x)
# y = Time(25, 98)
# (x.increment(25,12))
print(x)
print(str(x))
# print(help(Time))