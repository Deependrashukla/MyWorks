class Error(Exception):
	pass

class ZError(Error):
	pass

class RError(Error):
	pass


try :
	x = Error(5, 5)
	# print(x)
	raise x
except :
	print('Error 5', x)