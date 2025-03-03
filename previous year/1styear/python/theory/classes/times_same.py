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
		self._hour = hour
		self._minute = minute

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


		self._minute += minutes
		self._hour += (hours + self._minute // 60)
		self._minute = self._minute % 60
		self._hour = self._hour % 24


	def __repr__(self):
		return str(self.__class__) + ' (' + str(self._hour) + ', ' + str(self._minute) + ')'


	def getHour(self):
		return self._hour


	def setHour(self, value):
		"""
		"""
		assert type(value) == int
		assert 0 <= value < 24

		self._hour = value


	def getMinute(self):
		return self._minute

	def setMinute(self, minute):
		assert type(minute) == int 
		assert 0 <= minute < 60

		self._minute = minute


x = Time(2, 10)
# print(x._is_minute(10))
x.hour = 'hello'
x.setMinute(5)
print(x)
# print(x.setHour(5))
# print(x)
# y = Time(25, 98)
# (x.increment(25,12))
# print(x)
# print(help(Time))