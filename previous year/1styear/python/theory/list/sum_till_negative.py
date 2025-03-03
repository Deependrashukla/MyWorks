def lst_create(number_of_elements) :
	lst = []
	for j in range(number_of_elements) :
		inp = input('Enter your numbers :')
		lst.append(int(inp))
	return lst 
	

number_of_elements = int(input('Enter number of input you want to sum :'))


def sum_till_negative(lst) :
	total = 0
	for i in lst :
		if i >= 0 :
			total += i

		else :
			return total

	return total

print(sum_till_negative(lst_create(number_of_elements)))