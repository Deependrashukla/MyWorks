"""
Author :Sonal Kumari.
"""

s = input('Enter your string: ')
letter = input('Enter your letter which you have to find in string: ')

def print_words_count(string, letter):
	"""
	prints the words from the input string starting from the input letter and count of such words.
	input string should not end with a space.

	Parameter string :string given by user.
	Precondition :Input string should not end with a space and it contain atleast one letter.

	parameter letter :which letter you have to find in string given by user.
	precondition :You have to enter only first letter of word which you have to find.

	"""

	acc = 0                                   #created an accumulator for accumulating count of words starting with input letter
	if string[0] == letter :                  #checking if the input string start with the input letter
		space_index = string.find(' ')
		if space_index == -1 :                #special case when only one character is entered.
			space_index = len(s)
		print(string[:space_index])
		acc += 1

	for i in range(len(s)) :
		if string[i] == " " and string[i + 1] == letter :         #checking with help of spaces that the word starts with input letter or not
			space_index = string.find(' ', i + 1)
			if space_index == -1 :                                #checking if the string end with input letter 
				space_index = len(string)
			print(string[i + 1:space_index])
			acc += 1

	print(acc)


print_words_count(s, letter)