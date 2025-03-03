class Date():  # Fill in missing part
	"""A class representing a month, day and year
	Attribute MONTHS: A CLASS ATTRIBUTE list of all month abbreviations in order
	Attribute DAYS: A CLASS ATTRIBUTE that is a dictionary. Keys are the strings from MONTHS; values are days in that month ('Feb' is 28 days)"""
	# Attribute _year: The represented year. An int >= 2000 (IMMUTABLE)
	# Attribute _month: The month. A valid 3-letter string from MONTHS (IMMUTABLE)
	# Attribute _day: The day. An int representing a valid day of _month (MUTABLE)
	MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	DAYS = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
	def __init__(self,y, m, d):
		"""
		Initializes a new date for the given month, day, and year
		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month
		Precondition: d is an int and a valid day for month m
		"""
		assert type(y) == int and y >= 2000
		self._year = y 
		self._month = m 
		self.day = d 

	@property
	def year(self):
		"""
		Returns the year of this date
		"""
		return self._year

	@property
	def month(self):
		"""
		Returns the month of this date
		"""
		return self._month

	@property
	def day(self):
		"""
		Returns the day of this date
		"""
		return self._day 

	@day.setter
	def day(self, value):
		"""
		Sets the day of this date
		Parameter value: The new day
		Precondition: value is a valid day in the month
		"""
		assert type(value) == Date
		self._day = value

	def __str__(self): 
		"""
		Returns a string representation of this date.
		The representation is month day, year like this: 'Jan 2, 2002'
		"""
		return str(self._month) + ' ' + str(self._date) + ',' + str(self._year) 

	def __lt__(self,other):  # Fill in missing part
		"""
		Returns True if this date happened before other (False otherwise)
	
		Precondition: other is a Date
			
		This method causes a TypeError if the precondition is violated.
		"""
		if not isinstance(other,Date):
			t = TypeError(other)
			raise t

		if self._year < other._year:
			return True 
		elif self._year == other._year and Date.MONTHS.index(self._month) < Date.MONTHS.index(other._month):
			return True 
		elif self._year == other._year and Date.MONTHS.index(self._month) == Date.MONTHS.index(other._month) and self._day < other._day:
			return True 
		else:
			return False



	
# IMPORTANT: You are limited to 20 lines. Do NOT brute force this.
# Fill in missing part

class DateTime(Date):   # Fill in missing part
	"""A class representing a month, day and year, plus time of day (hours, minutes)"""
	# Attribute _hour: The hour of the day. An int in range 0..23 (MUTABLE)
	# Attribute _minute: The minute of the hour. An int in range 0..59 (MUTABLE)
	
	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.
	@property
	def hour(self):
		"""
		Returns the hour of the day

		"""
		return self._hour

	@hour.setter
	def hour(self,value):
		"""
		Sets the hour of the day
		Parameter value: The new hour
		Precondition: hour is an int in 0..23
		"""
		assert type(value._hour) == int , repr(value._hour) + 'not an integer'
		assert value._hour in range(0,24),repr(value._hour) + 'not in range(0,24)'
		self._hour = value 
	
	@property
	def minute(self):
		"""
		Returns the minute of the hour
		"""
		return self._minute
	
	@minute.setter
	def minute(self,value):
		"""
		Sets the minutes of the day
		Parameter value: The new minute
		Precondition: minute is an int in 0..59
		"""
		assert type(value._minute) == int ,repr(value._minute) + 'is not an integer'
		assert value._minute in range(0,60),repr(value._minute) + ' is not in range (0,60)'
		self._minute = value

	def __init__(y,m,d,hr = 0,mn = 0): # Fill in missing part
		"""
		Initializes a new datetime for the given month, day, year, hour and minute
		This method adds two additional (default) parameters to the initialize for
		Date. They are hr (for hour) and mn (for minute).
		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month
		Precondition: d is an int and a valid day for month m
		Precondition: hr is an int in the range 0..23 (OPTIONAL; default 0)
		Precondition: mn is an int in the range 0..59 (OPTIONAL; default 0)
		"""
		super().__init__(y,m,d)
		self.setHour(hr)
		self.setMinute(mn)

		


	def __str__(self): # Fill in missing part
		"""
		Returns a string representation of this DateTime object

		The representation is 'hh:mm on month day, year' like this: '9:45 on Jan 2, 2002'
		Single digit minutes should be padded with 0s. Hours do not need to be padded.

		"""

		return str(self._hour) + ':' + str(self._minute) + ' on ' + super().__str__(self)
	