'''
This function tells about that event1 going before,after or same at time reference to event2.

Author: Kirtan Khichi
Date:November 17,2022
'''
# time1=int(input('enetr your time1'))
# time2=int(input('enetr your time2'))
# suffix1=input('enetr your suffix1')
# suffix2=input('enetr your suffix2')
def find_chronology(time1,suffix1,time2,suffix2):
	'''
	Prints the events1 is before ,after or at a same time to event2

	event1 is assign to first two parameters and event2 is assign to last two parameter.
	Time describe by the first two parameter are compare by time describe by the last two parameter.
	Event1 is before the the event2 or at same time or after the event1.[same day required.]
	
	Parameter time1:give the time for event 1
	Precondition:enter time in non negative interger only.

	Parameter suffix1: suffix assign like as pm or am
	Precondition:suffix always be in string

	Parameter time2:give the time for event2
	Precondition:enter time in integer only

	Parameter suffix2:give the suffix like pm or am
	Precondition:suffix always be in string

	Examples:
	>>>find_chronology(3,am,4,am)
	event1 is 'before' event2
	>>>find_chronology(3,am,4,pm)
	event1 is 'before' event2
	>>>find_chronology(5,pm,4,pm)
	event1 is 'after' event2
	>>>find_chronology(3,am,3,am)
	event1 and  event2 timings are 'same'.
	>>>find_chronology(3,pm,4,am)
	event1 is 'after' event2
	'''
	if time1==time2 and suffix1==suffix2 :
		print('event 1 and event 2 timings are same')
	elif time1>time2 and suffix1==suffix2:
		print('event 1 is fiirst event')
	elif time2>time1 and suffix1==suffix2:
		print('event 2 is first event')
	elif time1==time2 and suffix1=='am' or suffix2=='pm':
		print('event 1 is the first event')
	elif time1==time2 and suffix1=='pm' or suffix2=='am':
		print('event 2 is the first event')

	else:
		print(time2,suffix2,'is the first event has to be done')
	
# find_chronology(time1,suffix1,time2,suffix2)
if __name__=='__main__':
	import doctest
	doctest.testmod() 



