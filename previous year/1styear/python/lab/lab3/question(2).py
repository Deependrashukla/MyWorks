'''
This whole program for checking the person is major or not.

Author: Kirtan Khichi
Date:November 17,2022

'''
#question (2)
gender=input('enter your gender')

#age=int(input('enter your age :- '))
year=int(input('enter your birth year :-'))
month=int(input('enter your month of birth'))
date=int(input('enetr your date of birth  '))


def age(year,month,date):
	'''
	Return:bool value for age.

	age has format 'year,month,date'
	the function will return a output in bool value.

	Parameter year:year of birth.
	Precondition:you have to enter year in interger only.

	parameter month:month of birth.
	precondition:you have to enter month in integer only.

	parameter date:date of birth.
	precondition:you have to enter date in interger only.
	Examples:
	>>>age(2003,10,10)
	True
	>>>age(2020,10,10)
	False
	>>>age(2004,10,3)
	False
	>>>age(2004,11,1)
	True
	'''
	return (year<2004 or year==2004 and (month<11 or (month==11 and date<3)))

def is_eligible(gender):
	'''
	Return:bool value for gender

	This function returns bool value for gender and gives the person is major or not.
	Here only two gender is 'male' and 'female'.

	Parameter gender:it define gender
	Precondition:youn have to enter your gender in string format only.
	Examples:
	>>>is_eligible('male')
	True
	>>>is_eligible('female')
	'''
	return (gender=='male' or age(year,month,date))
print(is_eligible(gender))
print(age(year,month,date))



 
