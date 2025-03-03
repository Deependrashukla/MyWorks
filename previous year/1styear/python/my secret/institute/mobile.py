def mobile1():
	global mobileno
	mobileno=int(input('enter your mobile number :-'))
	if len(str(mobileno))==10:
		pass
	else:
		print('enter your corect mobile number Please')
		mobile1()