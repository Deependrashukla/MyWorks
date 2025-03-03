# s=input('enetr your string :-')
from hypothesis import given, strategies as st, settings
def unique_vowels_in_word(s,case_sensitive=False):
	'''
	Return the number of unique vowels in string s.

	This function is design for calculating unique number of vowels.
	in this case if case_sensitive value is default then uppercase is equal to lower case.
	Otherwise upper case is not equal to lower case.
	If we inputed any type of number or any special character then functions gives -1.

	Examples:
	>>> unique_vowels_in_word('hii')
	1
	>>> unique_vowels_in_word('hiI')
	1
	>>> unique_vowels_in_word('AAEEIIOOUU')
	5
	>>> unique_vowels_in_word('AaEeIiOoUu')
	5
	>>> unique_vowels_in_word('AaEeIiOoUu',True)
	10
	>>> unique_vowels_in_word('AAEEIIOOUU',True)
	5
	>>> unique_vowels_in_word('hii1',True)
	-1
	>>> unique_vowels_in_word('A')
	1

	Parameter s:takes a string
	Precondition:You have to enter the in string and contains atleat one letter.

	Parameter case_sensitive:take a bool value
	Precondition:default value is false then uppercase=lowercase otherwise treated as different.


	'''
	
	if not(s.isalpha()):
		return -1
	else:
		if case_sensitive==False:
			s=s.lower()
			return (int('a' in s) + int('e' in s) +int('i' in s) +int('o' in s) +int('u' in s))
		else:
	
			return (int('a' in s) + int('e' in s) +int('i' in s) +int('o' in s) +int('u' in s) +int('A' in s) + int('E' in s) +int('I' in s) +int('O' in s) +int('U' in s))
	
# print(unique_vowels_in_word('A'))
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()
# print(unique_vowels_in_word(s))
def sol_unique_vowels_in_word(s, case_sensitive=False):
	if not s.isalpha():
		return -1
	vowels = 'aeiouAEIOU'
	if not case_sensitive:
		s = s.lower()
		return len(set(s).intersection(vowels))
	# if case_sensitive:
		# return (int('a' in s) + int('e' in s) +int('i' in s) +int('o' in s) +int('u' in s) +int('A' in s) + int('E' in s) +int('I' in s) +int('O' in s) +int('U' in s))
	
# # Use Hypothesis

# # Run plenty of examples!
@settings(max_examples=10000)
# # Test with default argument (False)
@given(st.text())
def test_1_arg(s):
	assert unique_vowels_in_word(s) == sol_unique_vowels_in_word(s)
@given(st.text(), st.booleans())
def test_2_arg(s, b):
	assert unique_vowels_in_word(s, b) == sol_unique_vowels_in_word(s, b)
# Run the Hypothesis
"""
s=input('enetr your string')
def vowels_alphabetical(s):
	'''
	Return:True for alphabetical order of vowels in s otherwise gives False.

	Here vowels means a,e,i,o,u or A,E,I,O,U
	In this function lower case and upper case are treated as same.

	Example:
	>>> vowels_alphabetical('abe')
	True
	>>> vowels_alphabetical('abae')
	True
	>>> vowels_alphabetical('abAE')
	True
	>>> vowels_alphabetical('ABCEIO')
	True
	>>> vowels_alphabetical('elephant')
	False
	>>> vowels_alphabetical('Elephant')
	False
	>>> vowels_alphabetical('AEIOUaeiou')
	True
	>>> vowels_alphabetical('AEIOUuoiea')
	False
	>>> vowels_alphabetical('sky')
	True

	Parameter s:Takes a value from user.
	Precondition:Writting value must be a string and must be a letter.
	'''
	a=s.find('a')
	e=s.find('e')
	i=s.find('i')
	o=s.find('o')
	u=s.find('u')
	if s.find('a')==-1:
		a=s.find('e')
	if s.find('e')==-1:
		e=s.find('i')
	if s.find('i')==-1:
		i=s.find('u')
	if s.find('o')==-1:
		o=s.find('u')
	if s.find('u')==-1:
		u=s.find('u')+1
	return a<=e<=i<=o<=u
print(vowels_alphabetical(s))
"""