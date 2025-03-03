"""This module contains test functions"""
import inspect
 
def assert_equals(expected,received):
	"""Quits with the msg if expected and receved differ

	Precondition: expected and received should not be floats"""

	if(expected!=received):
		print("Expected "+str(expected)+" but received "+str(received))
		previous_frame = inspect.currentframe().f_back
		(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
		print("Line "+str(line_number)+" of "+str(filename))
		print("Quitting with error")
		exit()



