coordinate_x = float(input('Enter your x-coordinate : '))
coordinate_y = float(input('Enter your y-coordinate : '))
def delivery(coordinate_x, coordinate_y):
	'''
	Prints swiggy will deliver if distance is less than 50 according to coordinates otherwise gives not diliver.

	Doctests:
	>>> delivery(0, 0)
	Swiggy will deliver to your address.
	>>> delivery(10, 10)
	Swiggy will deliver to your address.
	>>> delivery(200,200)
	Swiggy can not deliver to your address.
	'''
	distance = (coordinate_x ** 2 + coordinate_y ** 2) ** 0.5

	if distance <= 50 :
		print('Swiggy will deliver to your address.')
	else:
		print('Swiggy can not deliver to your address.')


delivery(coordinate_x, coordinate_y)