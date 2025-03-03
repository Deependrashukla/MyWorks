def name1():
	name=input('enter your name :- ')
	if not(name.isalpha()):
		print('enter your correct name please')
		name1()