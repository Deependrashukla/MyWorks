# # # for i in range(3, 10 ):
# # # 		x = ( ( i * '*' ) + (1 - 1 ) * '*' )   # Here we are making LHS of triangle.    
# # # 		y = ( (5 - i + 10 ) * '+' )    # Here we are making spaces according to number of rows and line width.
# # # 		z = ( (i-1) * '/' )                          # Here we are making RHS of triangle. 

# # 		# print(y+x+ z)

# # # for i in range(4):
# # # 	print('*'*)

# # def christmas(first_row, incr, number_rows, line_width) :

# # 	"""
# # 	Printing the christmas tree trinagle according to user inputs.

# # 	Line Width can not less than number_rows.

# # 	Parameter first_row : Number of asterisks('*') in first row given by user.
# # 	Precondition : Input must be integer.

# # 	Parameter incr : Increment of asterisks('*') given by user.
# # 	Precondition : Input must be integer.

# # 	Parameter num_rows : Number of rows in each traingle section given by user.
# # 	Precondition : Input must be integer.

# # 	Parameter line_width : Value given by user to shift the tree align.
# # 	Precondition : Input must be integer.

# # 	"""

# # 	for i in range(1, number_rows * incr + 1, incr) :
# # 		print(( (line_width - i - first_row // 2 + 1 ) * ' ') + (i * '*') + ((i - 1) * '*') + ( (first_row - 1) * '*') )



# # def christmas_stem(first_row, number_rows, line_width):
# # 	"""
# # 	Printing stem of christmas tree according to user inputs. 

# # 	Parameter first_row : Number of asterisks('*') in first row given by user.
# # 	Precondition : Input must be integer.

# # # 	Parameter num_rows : Number of rows in each traingle section given by user.
# # # 	Precondition : Input must be integer.

# # # 	Parameter line_width : Value given by user to shift the tree align.
# # # 	Precondition : Input must be integer.

# # # 	"""
# # # 	for i in range(number_rows) :
# # # 		print((line_width - first_row // 2) * ' ' + first_row * '*')

# # # christmas(1, 1, 5, 15)
# # # christmas(2, 1, 5, 15)
# # # christmas_stem(4, 3, 15)
# # # # christmas(3, 1, 5, 10)
# # # # christmas(4, 1, 5, 10)
# # # # christmas(5, 1, 5, 10)
# # # # christmas(6, 1, 5, 10)
# # # # christmas(7, 1, 5, 10)
# # # # christmas(8, 1, 5, 10)
# # # # christmas(9, 1, 5, 10)
# # # # christmas(10, 1, 5, 10)





# # # # def christmas(first_row, incr, number_rows, line_width) :
# # # # 	i = 0
# # # # 	for i in range(1, number_rows * incr + 1, incr) :
# # # # 		print((line_width - 2 * i ) + i * '*' + 1 * '+' )

# # # # christmas(3, 1, 5, 10)


# # # line_width = 10
# # # def christmas():
# # # 	for i in range(1,6):
# # # 		print((line_width - i)* 's'  + i * '*' + (i-1)*'*' )
# # # christmas()


# # def christmas(first_row, incr, number_rows, line_width) :

# # 	"""
# # 	Printing the christmas tree trinagle according to user inputs.

# # 	Line Width can not less than number_rows.

# # 	Parameter first_row : Number of asterisks('*') in first row given by user.
# # 	Precondition : Input must be integer.

# # 	Parameter incr : Increment of asterisks('*') given by user.
# # 	Precondition : Input must be integer.

# # 	Parameter num_rows : Number of rows in each traingle section given by user.
# # 	Precondition : Input must be integer.

# # 	Parameter line_width : Value given by user to shift the tree align.
# # 	Precondition : Input must be integer.

# # 	"""

# # 	for i in range(1, number_rows * incr + 1, incr) :
# # 		print(( (line_width - i - first_row // 2 + 1 ) * ' ') + (i * '*') + ((i - 1) * '*') + ( (first_row - 1) * '*') )

# # christmas(1,1,5,10)
# # christmas(3,1,5,10)





# def christmas(first_row, incr, number_rows, line_width) :
# 	for i in range(1, number_rows * incr + 1, incr):
# 		print((line_width - i - first_row // 2 + 1) * ' ' + i * '*' + (i - 1) * '*' + (first_row - 1) * '*')
# christmas(1, 1, 5, 10)
# christmas(5, 1, 5, 10)
# christmas(3, 1, 5, 10)
# # christmas(4, 1, 5, 10)
# # christmas(5, 1, 5, 10)
# # christmas(6, 1, 5, 10)
# # christmas(7, 1, 5, 10)



# def christmas_stem(first_row, number_rows, line_width):

# 	for i in range(number_rows) :
# 		print((line_width - first_row // 2) * ' ' + first_row * '*')

# christmas_stem(5, 5, 10)
def christmas(first_row, incr, num_rows, line_width):
	"""prints christmas tree using asterisk.

	parameter first_row: number of asterisk must be printed on first row.
	precondition: first_row must be a positive integer.

	parameter incr: increment of asterisk that every next line should follow.
	precondition: incr must be a positive integer and for trunk it should be 0.

	parameter num_rows: Total number of rows program should contain.
	precondition: num_rows must be a positive integer.

	parameter line_width: is the width of line about which program should be center aligned.
	precondition: line_width must be a positive integer.
	"""

	# check for incr input if odd make it even by adding one
	increment = incr
	if increment%2 != 0:
		increment = incr + 1

	# check for valid first_row input
	if first_row <= 0:
		print("invalid input: first line input should be positive integer")
		return

	# check for increment input in each following line
	if increment < 0:
		print("invalid input: increment should be 0 or positive integer")
		return

	# check for total no. of rows input
	if num_rows <= 0:
		print("invalid input: Total number of lines to be printed should be positive integer")
		return

	# check for line_width along which program has to center aligned with the last trapezoid
	if line_width < first_row + (increment * num_rows):
		print("invalid input: please increase the line width")
		return

	# now print rows in a loop
	for i in range(num_rows):
		num_asterisk = first_row + increment * i # asterisks in this line
		num_spaces = (line_width - num_asterisk) // 2 # spaces before asterisk
		print(' ' * num_spaces + '*' * num_asterisk)


christmas(1,3,10,100)
# christmas(17,3,10,100)
# christmas(27,3,10,100)
# christmas(10,0,5,100)