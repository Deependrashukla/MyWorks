'''coeff_x_squre=float(input('enter a number which is a leading coefficient of x**2'))
coeff_x=float(input('enter ytour number which of  a leading coefficient of x '))
constant=float(input('enter your constant number :-'))

def quadratic(coeff_x_squre,coeff_x,constant):
	#quad=(coeff_x_squre*x**2 + coeff_x*x + constant)

#	roots= (-coeff_x+((coeff_x**2 - 4*coeff_x_squre*constant)**0.5))/2*coeff_x_squre
	return ((-coeff_x+((coeff_x**2 - 4*coeff_x_squre*constant)**0.5))/2*coeff_x_squre , (-coeff_x-((coeff_x**2 - 4*coeff_x_squre*constant)**0.5))/2*coeff_x_squre)

x=print(quadratic(coeff_x_squre,coeff_x,constant))'''

'''
#question (2)
gender=input('enetr your gender')

#age=int(input('enter your age :- '))
year=int(input('enter your birth year :-'))
month=int(input('enter your moth iof birth'))
date=int(input('enetr '))


def age(year,month,date):
	>>>age(2003,10,10)
	True
	>>>age(2020,10,10)
	False
	return (year<2004 or year==2004 and (month<11 or (month==11 and date<3)))
#age1=age(year,month,date)
def is_eligible(gender ):
	>>>is_eligible('male')
	True
	>>>is_eligible('female')

	return (gender=='male' or age(year,month,date))
print(is_eligible(gender))
print(age(year,month,date)) '''

'''
>>>is_eligible('male')
True
>>>is_eligible('female')
>>>age(2003,10,10)
True


'''



'''def gender(gender,year,month,date):
	return gender == 'male' or year 

x=print(gender1(gender))

def dob(year):
	return (2022-year)>=18
y=print(dob(year))
def checking(year):
	x=='false'
	return(2022-2012)>=10
checking(year)'''




''' question(3)
score1=int(input('enter your number of boy'))
score2=int(input('enetr your number of boy'))
score3=int(input('enetr your number of girl'))
score4=int(input('enetr your number of girl'))
def boy_score(score1,score2):
	return (score1+score2)/2
def girl_score(score3,score4):
	return (score3+score4)/2
print((boy_score(score1,score2)+girl_score(score3,score4))/2)
'''




def func1():
	from mymodule import *
	n= x+1
	

n=3
func1()
print(n)



























#question (5)
def func1():
	x=5
	print("Inside func1, before calling func2: ",x)
	func2()
	print("Inside func1, after calling func2: ",x)

def func2():
	global x
	x=x*2

x=10
print("Initial: ",x)
func1()
print("After func1: ",x)
func2()
print("After func2: ",x)

'''
input x=10
output
>>>intial 10
>>>inside func1,before calling func2: 5
>>>20
>>>inside func1,before calling func2: 20
>>>after func2 :40
'''




