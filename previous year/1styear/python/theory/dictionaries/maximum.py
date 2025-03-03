# def maximum1():
# 	num = int(input('enter your number: '))
# 	maximum = num 
# 	while num!= -1:
# 		maximum = num
# 		num = int(input("Enter: "))
# 		if num > maximum:
# 			maximum = num


# 	return maximum

# print(maximum1())


def max_1():
	acc = [0]
	for i in acc :
		num = int(input('enter: '))
		if num == -1 :
			break 
		acc.append(i)

	return max(acc)

print(max_1())