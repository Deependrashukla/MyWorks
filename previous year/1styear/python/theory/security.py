from encryption import encryption
from dencryption import dencryption
user_string=input('Enter your string : ')
is_willing = input('you wants to decyrpt the data again if yes then put"y" otherwise "n" : ').lower()
def converter(target_string):
	return encryption(user_string)
	
if is_willing == 'y':
	print(dencryption(converter(user_string)))
elif is_willing == 'n' :
	pass
else:
	print('You have to Enter correct input')



