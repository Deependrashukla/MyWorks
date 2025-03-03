day = input( "enter weekday:" ).lower()
 
def is_weekday(day):
	"""
	Returns True if input day is weekday(except saturday and sunday), otherwise None.

	In this function weekends have saturday and sunday.Otherthan weekends are weekdays.
	Here days are Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday.

	Parameter day:It is day given by user.
	Precondition:Day must be valid as per description.

	Doctest:
	>>> is_weekday('monday')
	True
	>>> is_weekday('Monday')
	True
	>>> is_weekday('sunday')

	>>> is_weekday('Sunday')

	>>> is_weekday('SuNdAy')


	"""
	if not(day == "saturday" or day == "sunday") :
		return True

def alarm_time(day):
	"""
	Returns 7AM if input day is weekday,otherwise returns 9AM.

	Here the output returns value according to function is_weekday().
	Here days are Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday.

	Parameter day:It is day given by user.
	Precondition:Day must be valid as per description.

	"""
	if is_weekday (day) == None:
		return '9 AM'

	else:
		return '7 AM'	
print(alarm_time(day))




