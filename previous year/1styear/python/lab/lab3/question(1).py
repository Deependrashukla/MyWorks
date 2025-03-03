coeff_x_squre=float(input('enter a number which is a leading coefficient of x**2'))
coeff_x=float(input('enter ytour number which of  a leading coefficient of x '))
constant=float(input('enter your constant number :-'))

def quadratic(coeff_x_squre,coeff_x,constant):
	#quad=(coeff_x_squre*x**2 + coeff_x*x + constant)
	'''
	>>>quadratic(1,2,1)
	(1.0,1.0)
	>>>quadratic(1,1,1)
	
	'''

#	roots= (-coeff_x+((coeff_x**2 - 4*coeff_x_squre*constant)**0.5))/2*coeff_x_squre
	return ((-coeff_x+((coeff_x**2 - 4*coeff_x_squre*constant)**0.5))/2*coeff_x_squre , (-coeff_x-((coeff_x**2 - 4*coeff_x_squre*constant)**0.5))/2*coeff_x_squre)

x=print(quadratic(coeff_x_squre,coeff_x,constant))
