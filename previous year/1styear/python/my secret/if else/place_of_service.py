age=int(input('enter your age :- '))
sex=input('Enter your sex for male "M" or "m" for women "F" or "f" :- ').upper()
marital_status=input('Enter your marital_status for yes "Y" or "y" or for not married "n" or "N" :- ').upper()
if sex=='F':
	print('you work in urban area only!')
elif sex=='M' and age>=20 and age<40 :
	print('You can work anywhere')
elif sex=='M' and age>=40 and age<=60 :
	print('you can work only in urban area !')
else:
	print("error")
