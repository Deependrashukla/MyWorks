"""
This program is making christmas tree using asterisk('*')

Author : Sonal Kumari.
"""

first_row = int(input('Enter number of asterisk in first row: '))
incr = int(input('Enter your incriminant number: '))
num_rows = int(input('enter number of rows: '))
line_width = int(input('Enter line_width: '))
 
def christmas_tree(first_row, incr, num_rows, line_width) :
	"""
	Printing the christmas tree according to user inputs.

	Line Width can not less than number_rows.

	Parameter first_row : Number of asterisks('*') in first row given by user.
	Precondition : Input must be integer.

	Parameter incr : Increment of asterisks('*') given by user.
	Precondition : Input must be integer.

	Parameter num_rows : Number of rows in each traingle section given by user.
	Precondition : Input must be integer.

	Parameter line_width : Value given by user to shift the tree align.
	Precondition : Input must be integer.

	"""

	#Here we are print 1st triangular part
	for i in range(1, (num_rows ) * incr + 1, incr) :
		x = ( ( i * '*' ) + (first_row - 1 ) * '*' )  # Here we are making LHS of triangle.    
		y = ( (num_rows - i + line_width ) * ' ' )    # Here we are making spaces according to number of rows and line width.
		z = ( (i -1) * '*' )                          # Here we are making RHS of triangle. 

		print(y + x + z)

	#Here we are print 2nd triangular part
	for i in range(num_rows // 2, (num_rows ) * incr + 2, incr) : 
		x = ( ( i * '*' ) + (first_row - 1 ) * '*' )   # Here we are making LHS of triangle.
		y = ( (num_rows - i + line_width) * ' ' )      # Here we are making spaces according to number of rows and line width.
		z = ( (i - 1) * '*' )                          # Here we are making RHS of triangle.

		print(y + x + z)

	#Here we are print 3rd triangular part
	for i in range(num_rows // 2 + 2, (num_rows ) * incr + 4, incr) :
		x = ( ( i * '*' ) + (first_row - 1 ) * '*' )   # Here we are making LHS of triangle.
		y = ( (num_rows - i + line_width) * ' ' )      # Here we are making spaces according to number of rows and line width.
		z = ( (i - 1) * '*' )                          # Here we are making RHS of triangle.

		print(y + x + z)



	#Here we are printing stem according to the size of tree.
	#Here are adjusting the stem of the tree to maintain symmetrycity that why we use if else statements.
	if num_rows % 2 == 0 :
		for y in range(1, num_rows // 2 + 2 ) :
			#Here we are substracting 1 in first part of ( ) because we want less spaces. 
			print((line_width + num_rows // 2 - 1 ) * ' ' + (num_rows // 2 + first_row - 1) * '*' + (num_rows // 2 + 1) * '*')
	else:
		for y in range(1, num_rows // 2 + 2 ) :
			print((line_width + num_rows // 2 ) * ' ' + (num_rows // 2 + first_row - 1) * '*' + (num_rows // 2 + 1) * '*')
	
christmas_tree(first_row, incr, num_rows, line_width)