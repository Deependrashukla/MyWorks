# def main1():
# 	result = input('Enter : ')
# 	x = float(result)
# 	print('The next number is: ' + str(x + 1))
# if __name__ == '__main__':
# 	main1()



# try:
#     result = input('Enter : ')
#     x = float(result)
#     print('The next number is: ' + str(x + 1))
# except:
#     print('number is not ')


# s=input('enter yoyr number')
# def is_float(s):
# 	try : 
# 		x = float(s)
# 		return True
# 	except:
# 		return False

# if __name__ == '__main__':
# 	print(is_float(s))

# for i in range(5):
# 	def func(x, y):
# 		try:
# 			return func2(x, y)
# 		except:
# 			return float('inf')

# 	def func2(x, y):
# 		try:
# 			return func3(x, y)
# 		except:
# 			return 0.0

# 	def func3(x, y):
# 		return x/y

# 	if __name__ == '__main__':
# 		func(1, i)




# def func(x, y):
# 	try:
# 		return func2(x, y)
# 	except:
# 		return float('inf')

# def func2(x, y):
# 	try:
# 		return func3(x, y)
# 	except:
# 		return 0.0

# def func3(x, y):
# 	return x/y

# if __name__ == '__main__':
# 	func(1, i)




def first(x):
	print('Starting')
	try:
		second(x)
	except:
		print('caught at first')
	print('Ending first')

def second(x):
	print('second')
	third(x)
	print('ending second')

def third(x):
	print('Starting third.')
	assert x > 1
	print('Ending third')

first(3)
