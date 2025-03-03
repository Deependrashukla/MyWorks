"""
This program is making christmas tree using asterisk('*')

Author : Sonal Kumari.
"""

def christmas(first_row, incr, number_rows, line_width) :

	"""
	Printing the christmas tree triangle according to user inputs.

	Line Width can not less than number_rows.
	If we take 0 in first_row than it will start with one asterisks('*').

	Parameter first_row : Number of asterisks('*') in first row given by user.
	Precondition : Input must be positive integer.

	Parameter incr : Increment of asterisks('*') given by user.
	Precondition : Input must be positive integer.

	Parameter num_rows : Number of rows in each traingle section given by user.
	Precondition : Input must be positive integer.

	Parameter line_width : Value given by user to shift the tree align.
	Precondition : Input must be positive integer.

	"""
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
	if number_rows <= 0:
		print("invalid input: Total number of lines to be printed should be positive integer")
		return



	# check for line_width along which program has to center aligned with the last trapezoid
	if line_width < first_row + (increment * number_rows):
		print("invalid input: please increase the line width")
		return

	if incr == 0 :
		for i in range(number_rows) :
			print((line_width - first_row // 2) * ' ' + first_row * '*')

	else:
		for i in range(1, number_rows * incr + 1, incr) :
			print(( (line_width - i - first_row // 2 + 1 ) * ' ') + (i * '*') + ((i - 1) * '*') + ( (first_row - 1) * '*') )

christmas(1, 1, 5, 15)
christmas(3, 1, 5, 15)
christmas(5, 1, 5, 15)
christmas(5, 0, 3, 15)