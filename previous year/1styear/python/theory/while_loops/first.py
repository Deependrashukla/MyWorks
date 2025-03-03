# loop = True
# while loop :

# 	try:
# 		x= input('Enter your number :')
# 		y = float(x)
# 		print('Your number incriment by 1 is' + str(y + 1))
# 		loop = False
# 	except:
# 		print('This is not number!, try again!')


def sum_squares(n) :
	total = 0

	for x in range(n) :
		total += x*x

	return total


def sum_squares_while(n) :
	l = 0
	total = 0
	while n > l :
		print('start loop' + str(total + 1))
		total += l*l
		l += 1
		print('End loop' )

	return total

print(sum_squares(5), sum_squares_while(5))