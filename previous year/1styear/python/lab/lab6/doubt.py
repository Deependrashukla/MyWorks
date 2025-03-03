# '''
# This function calculate the number of unique vowels.

# Author: Kirtan Khichi
# Date:November 30,2022
# '''
# # s=input('enter your string')
# from hypothesis import given, strategies as st, settings
# def unique_vowels_in_word(s,case_sensitive=False):
# 	'''
# 	Return the number of unique vowels in string s.

# 	This function is design for calculating unique number of vowels.
# 	in this case if case_sensitive value is default then uppercase is equal to lower case.
# 	Otherwise upper case is not equal to lower case.
# 	If we inputed any type of number or any special character then functions gives -1.

# 	Examples:
# 	>>> unique_vowels_in_word('hii')
# 	1
# 	>>> unique_vowels_in_word('hiI')
# 	1
# 	>>> unique_vowels_in_word('AAEEIIOOUU')
# 	5
# 	>>> unique_vowels_in_word('AaEeIiOoUu')
# 	5
# 	>>> unique_vowels_in_word('AaEeIiOoUu',True)
# 	10
# 	>>> unique_vowels_in_word('AAEEIIOOUU',True)
# 	5
# 	>>> unique_vowels_in_word('hii1',True)
# 	-1
# 	>>> unique_vowels_in_word('A')
# 	1

# 	Parameter s:takes a string
# 	Precondition:You have to enter the in string and contains atleat one letter.

# 	Parameter case_sensitive:take a bool value
# 	Precondition:default value is false then uppercase=lowercase otherwise treated as different.


# 	'''
	
# 	if not(s.isalpha()):
# 		return -1
# 	else:
# 		if case_sensitive==False:
# 			s=s.lower()
# 			return (int('a' in s) + int('e' in s) +int('i' in s) +int('o' in s) +int('u' in s))
# 		else:
	
# 			return (int('a' in s) + int('e' in s) +int('i' in s) +int('o' in s) +int('u' in s) +int('A' in s) + int('E' in s) +int('I' in s) +int('O' in s) +int('U' in s))
	

# def sol_unique_vowels_in_word(s, case_sensitive=False):
# 	if not s.isalpha():
# 		return -1
# 	vowels = 'aeiouAEIOU'
# 	if not case_sensitive:
# 		s = s.lower()
# 		return len(set(s).intersection(vowels))
# 	if case_sensitive:
# 		return (int('a' in s) + int('e' in s) +int('i' in s) +int('o' in s) +int('u' in s) +int('A' in s) + int('E' in s) +int('I' in s) +int('O' in s) +int('U' in s))
	
# # # Use Hypothesis

# # Run plenty of examples!
# @settings(max_examples=1000)
# # # Test with default argument (False)
# @given(st.text())
# def test_1_arg(s):
# 	assert unique_vowels_in_word(s) == sol_unique_vowels_in_word(s)
# @given(st.text(), st.booleans())
# def test_2_arg(s, b):
# 	assert unique_vowels_in_word(s, b) == sol_unique_vowels_in_word(s, b)
# # Run the Hypothesis
# if __name__ == '__main__':
# 	test_1_arg()
# 	test_2_arg()
# a=e=i=o=u=0
# s='abcdefghijkl'
# if 'a' in s:
# 	a=(s.index('a'))
# if 'e' in s:
# 	e=(s.index('e'))
# if 'i' in s:
# 	i=(s.index('i'))
# if 'o' in s:
# 	o=(s.index('o'))
# if 'u' in s:
# 	u=(s.index('u'))
# if a<e and e<i:
# 	print('True')
# else:
# 	print('False')
'''
This function tells about that the vowels of string are in alphabetical order or not.

Author: Kirtan Khichi
Date:November 17,2022
'''
# s=input('enter your string :-')
# def vowels_alphabetical(s):
# 	'''
# 	Return:True for alphabetical order of vowels in s otherwise gives False.

# 	Here vowels means a,e,i,o,u or A,E,I,O,U
# 	In this function lower case and upper case are treated as same.

# 	Example:
# 	>>> vowels_alphabetical('abe')
# 	True
# 	>>> vowels_alphabetical('abae')
# 	True
# 	>>> vowels_alphabetical('abAE')
# 	True
# 	>>> vowels_alphabetical('ABCEIO')
# 	True
# 	>>> vowels_alphabetical('elephant')
# 	False
# 	>>> vowels_alphabetical('Elephant')
# 	False
# 	>>> vowels_alphabetical('AEIOUaeiou')
# 	True
# 	>>> vowels_alphabetical('AEIOUuoiea')
# 	True
# 	>>> vowels_alphabetical('sky')
# 	True

# 	Parameter s:Takes a value from user.
# 	Precondition:Writting value must be a string and must be a letter.
# 	'''
# 	s=s.lower()
# 	a=s.find('a')
# 	e=s.find('e')
# 	i=s.find('i')
# 	o=s.find('o')
# 	u=s.find('u')

# 	if s.find('e')==-1:
# 		e=a+1
# 	if s.find('i')==-1:
# 		i=e+2
# 	if s.find('o')==-1:
# 		o=i+3
# 	if s.find('u')==-1:
# 		u=o+4
	
# 	return a<e<i<o<u
# print(vowels_alphabetical(s))
# if __name__ == '__main__':
	# import doctest
	# doctest.testmod()
# s=input('enter your string :-')
# def vowels_alphabetical(s):
#     '''
#     Return:True for alphabetical order of vowels in s otherwise gives False.

#     Here vowels means a,e,i,o,u or A,E,I,O,U
#     In this function lower case and upper case are treated as same.

#     Example:
#     >>> vowels_alphabetical('abe')
#     True
#     >>> vowels_alphabetical('abae')
#     True
#     >>> vowels_alphabetical('abAE')
#     True
#     >>> vowels_alphabetical('ABCEIO')
#     True
#     >>> vowels_alphabetical('elephant')
#     False
#     >>> vowels_alphabetical('Elephant')
#     False
#     >>> vowels_alphabetical('AEIOUaeiou')
#     True
#     >>> vowels_alphabetical('AEIOUuoiea')
#     True
#     >>> vowels_alphabetical('sky')
#     True

#     Parameter s:Takes a value from user.
#     Precondition:Writting value must be a string and must be a letter.
#     '''
#     s=s.lower()
#     a=s.find('a')
#     e=s.find('e')
#     i=s.find('i')
#     o=s.find('o')
#     u=s.find('u')

#     if e==-1:
#         e=a
#     if i==-1:
#         i=e+a
#     if o==-1:
#         o=i+e+a
#     if u==-1:
#         u=o+i+e+a
    
#     return a<=e<=i<=o<=u
# print(vowels_alphabetical(s))
# s=input('enter your string :- ')
from hypothesis import given, strategies as st, settings
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
    True
    >>> vowels_alphabetical('sky')
    True

    Parameter s:Takes a value from user.
    Precondition:Writting value must be a string and must be a letter.
    '''
    s=s.lower()
    a=s.find('a')
    e=s.find('e')
    i=s.find('i')
    o=s.find('o')
    u=s.find('u')
    if not s.isalpha():
    	return -1
    if e==-1:
        e=a
    if i==-1:
        i=e
    if o==-1:
        o=i
    if u==-1:
        u=o
    
    return a<=e<=i<=o<=u
print(vowels_alphabetical+9)
# print(vowels_alphabetical(s))
# if __name__ == '__main__':
# 	import doctest
# 	doctest.testmod()
# def sol_vowels_alphabetical(s):
# 	'''tells about alphabetical order of vowel in s  
# 	return: bool value.

# 	parameter s : string 

# 	precondition: string contain at least 1 alphabet and nothing other than english alphabet  
# 	'''

# 	'''
# 	>>> vowels_alphabetical('appl')
# 	True 
# 	>>> vowels_alphabetical('apple')
# 	True
# 	>>> vowels_alphabetical('eye')
# 	True
# 	>>> vowels_alphabetical('elephant')
# 	Fals
# 	>>> vowels_alphabetical('aeiou')
# 	True
# 	#>>>vowels_alphabetical('bcdl')
# 	#0
# 	'''
# 	if s.isalpha()==False:
# 		return -1
# 	else:
# 		a=s.lower().find('a')
# 		e=s.lower().find('e')
# 		e=e if e>-1 else a
# 		i=s.lower().find('i')
# 		i=i if i>-1 else e
# 		o=s.lower().find('o')
# 		o=o if o>-1 else i
# 		u=s.lower().find('u')
# 		u=u if u>-1 else o






# 	return u>=o>=i>=e>=a
# @settings(max_examples=1000)
# @given(st.text())
# def test_sol(s):
# 	assert vowels_alphabetical(s)==sol_vowels_alphabetical(s)