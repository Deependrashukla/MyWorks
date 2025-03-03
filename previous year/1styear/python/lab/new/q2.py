from math import pi

radius1 = float(input('Enter your first radius  : '))
radius2 = float(input('Enter your second radius  : '))

def area(radius):
	'''
	Return area according to radius.

	Parameter radius:It is the radius of cirlce.
	Precondition:it may be int or float.
	>>> area(1)
	3.145762
	'''
	return pi * (radius) ** 2

def area_check(radius1, radius2):
	'''
	This function prints high if sum of area according to radius grater than 100,
	medium if in between 50  or equal to 100,otherwise low.

	Parameter radius1:It is the radius of circle 1
	Precondition:it may be int or float.
	Parameter radius2:It is the radius of circle 2
	Precondition:it may be int or float.

	Doctect:
	>>> area_check(5,5)
	High
	>>> area_check(1,1)
	Low
	>>> area_check(2,2)
	Medium

	'''

	area_circle1 = area(radius1) 
	area_circle2 = area(radius2) 

	if area_circle1 + area_circle2 > 100 :
		return 'High'
	elif 100 >= area_circle1 + area_circle2 > 50 :
		return 'Medium'
	else:
		return 'Low'

area_check(radius1, radius2)