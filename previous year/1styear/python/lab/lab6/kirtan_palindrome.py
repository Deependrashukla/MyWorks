'''
This function tells about the string is palindrome or not

Author: Kirtan Khichi
Date:November 30,2022
'''
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
	word is palindrome
	>>> palindrome('1IHi1')
	word is palindrome
	>>> palindrome('IHI')
	word is palindrome

	Parameter word:take a string value from user.
	Precondition:word should be in string only and the casses may be ignored.
	If any thing enter otherwise english latter will give not a palindrome
	'''
	word=word.lower()
	if word==word[::-1]:
		print('word is palindrome')
	else:
		print('word is not a palindrome')
if __name__=='__main__':
	import doctest
	doctest.testmod()