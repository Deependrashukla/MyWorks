
# def max_grade(grades, cutoff) :

# 	lst = []
	
# 	# return max(grades.values())
# 	for i in grades :
# 		if grades[i] > cutoff :
# 			lst.append(i)

# 	return lst
# print(max_grade({'a' : 1,'b' : 5}, 0))



def give_extra_credits(grades, rolls, bonus) :

	# lst = []
	
	# return max(grades.values())
	for i in grades :
		if i in rolls :
			grades[i] = grades[i] + bonus

	return grades
print(give_extra_creditsi({'a' : 1,'b' : 5}, 'b,a', 50))
