def prompt(prompt1, valid):
	# loop = True
	# i = 0
	# while loop :
	# 	prompt2 = input(prompt1)
	# 	if prompt2 in valid :
	# 		loop = False
	# 	# i += 1
			
	# return prompt2
	response = input(prompt1)
	while not(response in valid) :


# prompt1 = input('Enter your name ')
valid = ('kirtan','deep','sonal','harsh')
print(prompt('Enter your name', valid))
