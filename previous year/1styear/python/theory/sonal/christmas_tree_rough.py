# def christmas_tree(first_row, incr, num_rows, line_width) :
# 	for i in range(1, num_rows+1) :
# 		x = (num_rows - i)

# 		print((x + line_width) * ' ' * incr + '*' * i * incr + (i-1) * '*' * (incr))

# 	for y in range(1, num_rows // 2 + 2 ) :
# 		# z = (num_rows)
# 		print((line_width*2 + incr*i*2 // 4 - 1 ) * ' ' + incr * (i//2) * '*' + incr * (i//2) * '*')
# 		# return (x * ' ' + '*' * i + (i-1) * '*')

# christmas_tree(1, 2, 10, 10)

# def christmas_tree(first_row, incr, num_rows, line_width) :
# 	for i in range(1, num_rows + 1) :
# 		x = ( i * '*' ) + (first_row - 1 ) * '*' 
# 		y = ( (num_rows - i ) * ' ' )
# 		z = ( (i - 1) * '*' )
# 		# print(first_row * '*')
# 		print(y + x + z)

# christmas_tree(1, 1, 10, 1)
first_row=int(input('Enter your first row number : '))
incr = int(input('Enter your incriminant number : '))
num_rows = int(input('enter number of rows : '))
line_width = int(input('Enter line_width : '))
 
def christmas_tree(first_row, incr, num_rows, line_width) :

	#Here we are print 1st triangular part
	for i in range(1, (num_rows )*incr, incr) :
		x = ( i * '*' ) + (first_row - 1 ) * '*'
		y = ( (num_rows - i + line_width ) * ' ' )
		z = ( (i -1) * '*' )
		# for i in range(1,num_rows+1,incr) :
			# print((num_rows-i+line_width)*' ' + ( i * '*' ) + (first_row - 1 ) * '*' +  ( (i -1) * '*' ))

		print(y + x + z)

	#Here we are print 2nd triangular part
	for i in range(num_rows//2, (num_rows )*incr +2, incr) :
		x = ( i * '*' ) + (first_row - 1 ) * '*' 
		y = ( (num_rows - i + line_width) * ' ' )
		z = ( (i - 1) * '*' )

		print(y + x + z)

	#Here we are print 3rd triangular part
	for i in range(num_rows//2 +2, (num_rows )*incr +4, incr) :
		x = ( i * '*' ) + (first_row - 1 ) * '*' 
		y = ( (num_rows - i +line_width) * ' ' )
		z = ( (i - 1) * '*' )

		print(y + x + z)



	#Here we are printing stem according to the size of tree
	if num_rows % 2 == 0 :
		for y in range(1, num_rows // 2 + 2 ) :
			print((line_width + num_rows // 2 - 1 ) * ' ' + (num_rows//2 + first_row - 1) * '*' + (num_rows//2+1) * '*')
	else:
		for y in range(1, num_rows // 2 + 2 ) :
			print((line_width + num_rows // 2 ) * ' ' + (num_rows//2 + first_row - 1) * '*' + (num_rows//2+1) * '*')
	
christmas_tree(first_row, incr, num_rows, line_width)



