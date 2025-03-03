coordinate_x = float(input('Enter your x-coordinate : '))
coordinate_y = float(input('Enter your y-coordinate : '))
coor_x = float(input('Enter x coordinate of restaurent : '))
coor_y = float(input('Enter y coordinate of restaurent : '))

def delivery(coordinate_x, coordinate_y):
	'''
	Prints swiggy will deliver if distance is less than 50 according to coordinates otherwise gives not diliver.

	Parameter coordinate_x:coordinate given by user.
	Precondition:coordinate must be int or float.

	Parameter coordinate_y:coordinate given by user.
	Precondition:coordinate must be int or float.

	Doctests:
	>>> delivery(0, 0)
	You are already in restaurent.
	>>> delivery(10, 10)
	Swiggy will deliver to your address.
	>>> delivery(200,200)
	Swiggy can not deliver to your address.
	>>> delivery(-5, -5)
	Swiggy will deliver to your address.
	'''
	distance = ((coordinate_x - coor_x) ** 2 + (coordinate_y - coor_y) ** 2) ** 0.5

	if distance == 0 :
		print('You are already in restaurent.')
	elif distance <= 50 :
		print('Swiggy will deliver to your address.')
	else:
		print('Swiggy can not deliver to your address.')


delivery(coordinate_x, coordinate_y)