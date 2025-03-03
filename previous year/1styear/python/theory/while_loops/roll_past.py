import random  
def roll_past(goal):
	
	total = 0
	while total < goal :
		x = random.randint(1, 6) 
		print(x)
		if x==1 :
			return 0
		total += x 

	return total

print(roll_past(10)) 