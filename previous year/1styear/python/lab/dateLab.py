class Date(object):
	MONTHS=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',  'Dec']
	DAYS={'Jan':31,'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}

	def isleapyear(self):
		if self._year%4==0:
			if self._year%100==0 and self._year%400 == 0:
				return True
			else:
				return False
			return True
		else:
			return False


	@property
	def year(self):
		return self._year

	@property
	def month(self):
		return self._month
	
	

	@property
	def day(self):
		return self._day

	@day.setter
	def day(self,value):
		if self.isleapyear == True:
			c=Date.DAYS[self._month]
		else:
			if self._month == 'Feb':
				c=29
			else:
				c=Date.DAYS[self._month]
		assert 0<value<= c
		self._day= value



	def __init__(self,y,m,d):
		self._year=y
		self._month = m
		self.day=d



	def __str__(self):
		return '('+str(self._year)+', '+str(self._month)+', '+str(self._day)+')'

	def __lt__(self,other):


		if not isinstance(other,Date):
			raise TypeError()

		if self._year < other._year:
			return True
		elif self._year == other._year and Date.MONTHS.index(self._month) < Date.MONTHS.index(other._month):
			return True
		elif Date.MONTHS.index(self._month) <= Date.MONTHS.index(other._month) and self._day<= other._day:
			return True
		else:
			return False



class DateTime(Date):



	@property
	def hour(self):
		return self._hour

	@property
	def minute(self):
		return self._minute

	@ hour.setter
	def hour(self,value):
		assert 0<= value <=23 ,'out of range'
		self._hour = value

	@ minute.setter
	def minute(self,value):
		assert 0<= value <=59, 'out of range'
		self._minute = value

	def __init__(self,y,m,d,h,minu):
		super().__init__(y,m,d)
		self.hour=h
		self.minute=minu

	def __str__(self):

		return "'"+str(self.hour)+':'+str(self.minute)+ ' on '+str(self.month)+' '+str(self.day)+', '+str(self.year)+"'"





d1=DateTime(2004,'Feb',29,23,45)
d2=Date(2001,'Feb',9)
print(d1<d2)
print(d1.month)