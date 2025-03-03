'''
This function tells about that the vowels of string are in alphabetical order or not.

Author: Kirtan Khichi
Date:December 1,2022
'''
s=input('enter your word :- ')
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
    
    if e==-1:
        e=a
    if i==-1:
        i=e
    if o==-1:
        o=i
    if u==-1:
        u=o
    
    return a<=e<=i<=o<=u
print(vowels_alphabetical(s))