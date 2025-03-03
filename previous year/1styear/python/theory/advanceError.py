def main():
	try:
		val = input('Enter ')
		x = float(val)
		print('The next number is ' + str(x + 1))
		assert x < 10, 'Out of range'

	except ValueError :
		print('Hey! That is not a number')

	except AssertionError :
		print('Out of Bounds')

if __name__=='__main__':
	main()