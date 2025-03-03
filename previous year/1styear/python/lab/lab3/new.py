from hypothesis import given,strategies as st
def middle(text):
	'''
	Return:middle 3rd of text

	The middle starts at the lenght divided by 3
	(rounded down) and continues until 2/3 of the 
	string rounded down.

	Parameter text:the string slice
	precondition:text is a string

	>>> middle('a')
	''
	>>> middle('ab')
	'a'
	>>> middle('abc')
	'b'
	>>> middle('abcde')
	'bc'
	>>> middle('12345')
	'23'
	>>> middle('abcdef')
	'cd'
	>>> middle('!@#$%')
	'@#'
	>>> middle('')
	''
	''' 
	size=len(text)
	start=size//3
	end=2*size//3
	result=text[start:end]
	return result
"""
def number_vowels(word):
	'''
	Return : number of vowels in string word

	>>> number_vowels('a')
	2
	>>> number_vowels('aa')
	2
	>>> number_vowels('put')
	1
	>>> number_vowels('but')
	1
	>>> number_vowels('aeiou')
	5
	>>> number_vowels('A')
	1
	>>> number_vowels('aA')
	2
	>>> number_vowels('AEIOU')
	5
	>>> number_vowels('AEIOUaeiou')
	10
	>>> number_vowels('sky')
	0

	Parameter word:The text to check  for vowels
	Precondition:word strings w/ at least one letter and only letters
	'''	
	
	
	a=word.count('a')+word.count('A')
	e=word.count('e')+word.count('E')
	i=word.count('i')+word.count('I')
	o=word.count('o')+word.count('O')
	u=word.count('u')+word.count('U')
	# return a+e+i+o+u
	print(a+e+i+o+u)"""

import math
def sol_middle(text):
	start=math.floor(len(text)/3)
	end=math.floor(2*len(text)/3)
	result=text[start:end]
	return result
'''
if __name__=='__main__':
	import doctest
	doctest.testmod()
'''
@given(st.text(min_size=2))
def test_number_vowels(text):
	# assert number_vowels('a')==sol_number_vowels('a')
	# assert number_vowels('aa')==sol_number_vowels('aa')
	# assert number_vowels('put')==sol_number_vowels('put')
	# assert number_vowels('but')==sol_number_vowels('but')
	# assert number_vowels('sky')==sol_number_vowels('sky')
	# assert number_vowels('aeiou')==sol_number_vowels('aeiou')
	# assert number_vowels('AEIOUaeiou')==sol_number_vowels('AEIOUaeiou')
	assert middle(text)==sol_middle(text)
