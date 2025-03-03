# def christmas_tree(first_row, incr, num_rows, line_width) :
# 	for i in range(1, num_rows) :
# 		x= (num_rows - i)

# 		print(x * ' ' + '*' * i  + (i-1) * '*')

# 	for y in range(1, num_rows // 2 + 1) :
# 		z=(num_rows-y)
# 		print(line_width * ' ' + z * '*' + (y - 1) * '*')
# 		# return (x * ' ' + '*' * i + (i-1) * '*')

# christmas_tree(1, 5, 10, 5)


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
# 		y = ( (num_rows - i + line_width ) * ' ' )
# 		z = ( (i - 1) * '*' )
# 		# print(first_row * '*')
# 		print(y + x + z)

# 	for i in range(num_rows//2, num_rows + 1) :
# 		x = ( i * '*' ) + (first_row - 1 ) * '*' 
# 		y = ( (num_rows - i + line_width) * ' ' )
# 		z = ( (i - 1) * '*' )
# 		# print(first_row * '*')
# 		print(y + x + z)

# 	for i in range(num_rows//2, num_rows + 1) :
# 		x = ( i * '*' ) + (first_row - 1 ) * '*' 
# 		y = ( (num_rows - i +line_width) * ' ' )
# 		z = ( (i - 1) * '*' )
# 		# print(first_row * '*')
# 		print(y + x + z)

# 	if num_rows % 2 == 0 :
# 		for y in range(1, num_rows // 2 + 2 ) :
# 			print((line_width + num_rows // 2 - 1 ) * ' ' + (num_rows//2 + first_row - 1) * '*' + (num_rows//2+1) * '*')
# 	else:
# 		for y in range(1, num_rows // 2 + 2 ) :
# 			print((line_width + num_rows // 2 ) * ' ' + (num_rows//2 + first_row - 1) * '*' + (num_rows//2+1) * '*')
	
# christmas_tree(2, 1, 5, 1)
# # even dal ne mai sahi print ho raha hai.
# jab mai first row ki value change kar raha hu toh dikkkat ho ja rahi hai.

def christmas_tree(first_row, incr, num_rows, line_width) :
	for i in range(1, num_rows + 1) :
		x = ( i * '*' ) + (first_row - 1 ) * '*' 
		y = ( (num_rows - i + line_width ) * ' ' )
		z = ( (i - 1) * '*' )

		print(y + x + z)

	for i in range(num_rows//2, num_rows + 1) :
		x = ( i * '*' ) + (first_row - 1 ) * '*' 
		y = ( (num_rows - i + line_width) * ' ' )
		z = ( (i - 1) * '*' )

		print(y + x + z)

	for i in range(num_rows//2, num_rows + 1) :
		x = ( i * '*' ) + (first_row - 1 ) * '*' 
		y = ( (num_rows - i +line_width) * ' ' )
		z = ( (i - 1) * '*' )

		print(y + x + z)

	if num_rows % 2 == 0 :
		for y in range(1, num_rows // 2 + 2 ) :
			print((line_width + num_rows // 2 - 1 ) * ' ' + (num_rows//2 + first_row - 1) * '*' + (num_rows//2+1) * '*')
	else:
		for y in range(1, num_rows // 2 + 2 ) :
			print((line_width + num_rows // 2 ) * ' ' + (num_rows//2 + first_row - 1) * '*' + (num_rows//2+1) * '*')
	
christmas_tree(1, 9, 5, 50)