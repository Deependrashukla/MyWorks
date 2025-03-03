
gender=input('enetr your gender')

#age=int(input('enter your age :- '))
year=int(input('enter your birth year :-'))
month=int(input('enter your moth iof birth'))
date=int(input('enetr '))
def age(year,month,date):
	return (year<2004 or year==2004 and (month<11 or (month==11 and date<3)))
#age1=age(year,month,date)
def is_eligible(gender ):
	return (gender=='male' or age(year,month,date))
print(is_eligible(gender))
print(age(year,month,date)) 


'''
def is_eligible(gender,year,month,date):
	return (gender=='male' or (year<2004 or year==2004 and (month<11 or (month==11 and date<3))))
print(is_eligible('female',2001,12,10))
'''


