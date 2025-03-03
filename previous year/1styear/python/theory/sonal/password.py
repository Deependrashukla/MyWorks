string = input('Enter your password to encrypt. : ')
def encryption(string):
	if '1' in string :
		string = string.replace('1', '@')
	if '2' in string :
		string = string.replace('2', '#')
	if '3' in string :
		string = string.replace('3', '₹')
	if '4' in string :
		string = string.replace('4', '_')
	if '5' in string :
		string = string.replace('5', '&')
	if '6' in string :
		string = string.replace('6', '-')
	if '7' in string :
		string = string.replace('7', '+')
	if '8' in string :
		string = string.replace('8', '(')
	if '9' in string :
		string = string.replace('9', ')')
	if '0' in string :
		string = string.replace('0', '/')
	# print(string)
	return string
print(encryption(string))

is_willing = input('if you want to decrypt the sequence then type "yes" ,otherwise "no" : ').lower()

def dencryption(string):
	if '@' in string :
		string = string.replace('@', '1')
	if '#' in string :
		string = string.replace('#', '2')
	if '₹' in string :
		string = string.replace('₹', '3')
	if '_' in string :
		string = string.replace('_', '4')
	if '&' in string :
		string = string.replace('&', '5')
	if '-' in string :
		string = string.replace('-', '6')
	if '+' in string :
		string = string.replace('+', '7')
	if '(' in string :
		string = string.replace('(', '8')
	if ')' in string :
		string = string.replace(')', '9')
	if '/' in string :
		string = string.replace('/', '0')
	# print(string)
	return string
	

if is_willing == 'yes' :
	print(dencryption(encryption(string)))


