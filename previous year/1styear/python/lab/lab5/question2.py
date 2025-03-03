'''
This function tells about that the vowels of string are in alphabetical order or not.

Author: Kirtan Khichi
Date:November 17,2022
'''
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
	if s.find('a')!=-1:
		if s.find('e')!=-1:
			if s.find('i')!=-1:
				if s.find('o')!=-1:
					if s.find('u')!=-1:
						return a<e<i<o<u
					else:
						return a<e<i<o
				else:
					return a<e<i
			else:
				return a<e
		# else:
			# return True
	return a<e<i<o<u
	

	
print(vowels_alphabetical(s))
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()
