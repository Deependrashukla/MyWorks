'''
This function tells about the string is palindrome or not

Author: Kirtan Khichi
Date:November 17,2022
'''
word=input('enter your string which you have to check is palindrome or not :- ')
def palindrome(word):
	'''
	print that string is palindrome or not.

	This function is to find that any string is palindrome or not.
	If any thing enter otherwise english latter will give not a palindrome.

	Examples:
	>>> palindrome('ihi')
	word is palindrome
	>>> palindrome('ihI')
	word is palindrome
	>>> palindrome('abb')
	word is not a palindrome
	>>> palindrome('1aba1')
	word is not a palindrome
	>>> palindrome('IHI')
	word is palindrome

	Parameter word:take a string value from user.
	Precondition:word should be in string only and the casses may be ignored.
	If any thing enter otherwise english latter will give not a palindrome
	'''
	# s=word==word[::-1]
	if word==word[::-1]:
		print('word is palndrome')
	else:
		print('word is not a palindrome') 
palindrome(word)
