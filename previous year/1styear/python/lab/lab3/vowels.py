from hypothesis import given,strategies as st,settings

def number_vowels(word):
	'''
	Return : number of vowels in string word

	>>> number_vowels('a')
	1
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
	return a+e+i+o

'''
if __name__=='__main__':
	import doctest
	doctest.testmod()

'''


def sol_number_vowels(word):
	'''
	>>> number_vowels('a')
	1
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
	'''
	a=word.count('a')+word.count('A')
	e=word.count('e')+word.count('E')
	i=word.count('i')+word.count('I')
	o=word.count('o')+word.count('O')
	u=word.count('u')+word.count('U')
	return a+e+i+o+u


@settings(max_examples=1000)
@given(st.text(min_size=3))
def test_number_vowels(word):
	# assert number_vowels('a')==sol_number_vowels('a')
	# assert number_vowels('aa')==sol_number_vowels('aa')
	# assert number_vowels('put')==sol_number_vowels('put')
	# assert number_vowels('but')==sol_number_vowels('but')
	# assert number_vowels('sky')==sol_number_vowels('sky')
	# assert number_vowels('aeiou')==sol_number_vowels('aeiou')
	# assert number_vowels('AEIOUaeiou')==sol_number_vowels('AEIOUaeiou')
	assert number_vowels(word)==sol_number_vowels(word)
