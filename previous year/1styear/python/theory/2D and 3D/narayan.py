'''
this contains a function is_interior

Author : Narayan Jat
Date:December 9,2022
'''
# Importing point module for point class
import point as t

def is_rectangle(d1,d2,d3,d4):
	'''
	Return :True If the points d1,d2,d3,d4 form a rectangle otherwise False

	Where d1,d2,d3 and d4 are points of rectangle.

	parameters d1: One point to define rectangle
	precondition : It is a point object

	parameters d2: Second point to define rectangle
	precondition : it is a point object

	parameters d3: third point to define rectangle
	precondition : it is a point object

	parameters d4: forth point to define rectangle
	precondition : it is a point object.

	Doctests:
	>>> is_rectangle(t.Point3(4,5,0),t.Point3(8,2,0),t.Point3(2,3,0),t.Point3(5,6,0))
	True
	>>> is_rectangle(t.Point3(4,5,0),t.Point3(8,2,0),t.Point3(2,3,0),t.Point3(5,2,0))
	False
	>>> is_rectangle(t.Point3(4,5,0),t.Point3(8,2,0),t.Point3(2,3,0),t.Point3(7,6,0))
	False
	>>> is_rectangle(t.Point3(4,5,0),t.Point3(8,2,0),t.Point3(2,3,0),t.Point3(3,2,0))
	True
	'''

	#rectangle is named as d1d2d3d4 so checking width equal,length equal,length not equal to width and diagonals are equal.
	if d1.distance(d2)==d3.distance(d4) and d2.distance(d3)==d1.distance(d4) and d1.distance(d3)==d2.distance(d4): 
		return True
	return False

# if _name=='main_':
# 	import doctest as he
# 	he.testmod()

def is_inside(d1,d2,d3,d4,p):
	'''
	Return:true if the p lies inside a rectangle otherwise false.

	If point lies on edges of rectangle the it will considered inside the rectangle

	parameters p:It is point to be checked.
	precondition: It is point object

	Doctests:
	>>> is_inside(t.Point3(4,5,6))
	'''

	if not(is_rectangle(d1,d2,d3,d4)):
		return "Your points don't form any possible rectangle please change coordinates"
	else:
		#calculating area of individual triangle with help of heron's formula
		p1=p.distance(d1) # distance of p from d1
		p2=p.distance(d2) # distance of p from d2
		p3=p.distance(d3) # distance of p from d3
		p4=p.distance(d4) # distance of p from d4
		w=d1.distance(d4) # width of rectangle
		l=d1.distance(d2) # length of rectangle
		s1=(p1+p2+l)/2   
		s2=(p2+p3+w)/2
		s3=(p3+p4+l)/2
		s4=(p4+p1+w)/2
		# x1=(((k1)))
		x1=round(((s1)*(s1-p1)*(s1-p2)*(s1-l))**(1/2)+((s2)*(s2-p2)*(s2-p3)*(s1-w))**(1/2)+((s3)*(s3-p3)*(s3-p4)*(s3-l))**(1/2)+((s4)*(s4-p4)*(s4-p1)*(s4-w))**(1/2))
		
		a1=round(l*w,10)
		return a1
d1=t.Point3(float(input("Enter x :")),float(input("Enter y :")),float(input("Enter z :")))
d2=t.Point3(float(input("Enter x :")),float(input("Enter y :")),float(input("Enter z :")))
d3=t.Point3(float(input("Enter x :")),float(input("Enter y :")),float(input("Enter z :")))
d4=t.Point3(float(input("Enter x :")),float(input("Enter y :")),float(input("Enter z :")))
p=t.Point3(float(input("Enter x :")),float(input("Enter y :")),float(input("Enter z :")))
print(is_inside(d1,d2,d3,d4,p))