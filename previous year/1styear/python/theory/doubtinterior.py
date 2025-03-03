# import point
# d1=point.Point3(float(input('enter your first point of 1:- ')),
# 	float(input('enter your second point of 1:- ')),float(input('enter your third  point of 1:- ')))
# d2=point.Point3(float(input('enter your first point of 2:- ')),
# 	float(input('enter your second point of 2 :- ')),float(input('enter your third  point of 2:- ')))
# p=point.Point3(float(input('enter your first point :- ')),
# 	float(input('enter your first point :- ')),float(input('enter your first point :- ')))


# def is_interior(p1,p2,p3):
# 	'''
# 	Return True if point p is inside cuboid otherwise gives False.

# 	Here d1 is any point of cuboid which consist (x1,x2,x3) points and d2 is point just opposite to d1 point consisting
# 	of (x2,y2,z2).p is the point which we have to check either inside the cuboid or not.

# 	'''
# 	return ((d1.x<=p.x or d1.x>=p.x)and (d2.x>=p.x or d2.x<=p.x) 
# 		and( d1.y<=p.x or d1.y>=p.x )and (d2.y>=p.y or d2.y<=p.y)and 
# 		(d1.z<=p.z or d1.z>=p.z )and (d2.z>=p.z or d2.z<=p.z))
# print(is_interior(d1,d2,p))







# x1=float(input('enter your first point of 1:- '))
# y1=float(input('enter your second point of 1:- '))
# z1=float(input('enter your third  point of 1:- '))
# x2=float(input('enter your first point of 2:- '))
# y2=float(input('enter your second point of 2 :- '))
# z2=float(input('enter your third  point of 2:- '))
# x3=float(input('enter your first point :- '))
# y3=float(input('enter your first point :- '))
# z3=float(input('enter your first point :- '))
# p1.x=x1
# p1.y=y1
# p1.z=z1
# p2.x=x2
# p2.y=y2
# p2.z=z2
# p3.x=x3
# p3.y=y3
# p3.z=z3








"""

'''
This programs tells about the point p is inside the cuboid or not.

Author: KIRTAN KHICHI
Date:December 4,2022
'''
import point
d1=point.Point3(0,0,0)
d2=point.Point3(0,0,0)
p=point.Point3(0,0,0)
#x1,y1,z1 is coordinate points of first diagonal point.
x1=float(input('enter your x point of one diagonal point:- '))  
y1=float(input('enter your y point of one diagonal point:- '))
z1=float(input('enter your z point of one diagonal point:- '))
#x2,y2,z2 is coordinate points of another diagonal point.
x2=float(input('enter your x point of opposite diagonal to first point:- '))
y2=float(input('enter your y point of opposite diagonal to first point:- '))
z2=float(input('enter your z point of opposite diagonal to first point:- '))
#x3,y3,z3 is coordinate points of point p which we have to check.
x3=float(input('enter your first point :- '))
y3=float(input('enter your first point :- '))
z3=float(input('enter your first point :- '))
d1.x=x1
d1.y=y1
d1.z=z1
d2.x=x2
d2.y=y2
d2.z=z2
p.x=x3
p.y=y3
p.z=z3
def is_interior(d1,d2,p):
	'''
	Return True if point p is inside cuboid otherwise gives False.

	Here d1 is any point of cuboid which consist (x1,x2,x3) points and d2 is point just opposite to d1 point consisting
	of (x2,y2,z2).p is the point which we have to check either inside the cuboid or not.Here we are assuming that 
	any point on cuboid consider as inside the cuboid.

	parameter d1:takes float value of coordinates of one diagonal point from user.
	precondition:d1 value must be numeric value.

	parameter d2:takes float value of coordinates of another diagonal point opposite to first one from user.
	precondition:d2 value must be numeric value.

	parameter p:takes float value of coordinate point p from user which we have to check.
	precondition:d1 value must be numeric value.

	'''
	return d1.x<=p.x and d2.x>=p.x and d1.y<=p.x and d2.y>=p.y and d1.z<=p.z and d2.z>=p.z

print(is_interior(d1,d2,p))

# d1=(p1.x=x1,p1.y=y1,p1.z=z1)
# d2=(p2.x=x2,p2.y=y2,p2.z=z2)
# d3=(p3.x=x3,p3.y=y3,p3.z=z3)

"""



"""

'''
This programs tells about the point p is inside the cuboid or not.

Author: KIRTAN KHICHI
Date:December 4,2022
'''
import point
d1=point.Point3(float(input('enter your x coordinate of one diagonal point:- ')),float(input('enter your y point of one diagonal point:- ')),float(input('enter your z coordinate of one diagonal point:- ')))
d2=point.Point3(float(input('enter your x coordinate of opposite diagonal to first point:- ')),float(input('enter your y coordinate of opposite diagonal to first point:- ')),float(input('enter your z coordinate of opposite diagonal to first point:- ')))
p=point.Point3(float(input('enter your x coordinate of point p :- ')),float(input('enter your y coordinate point p :- ')),float(input('enter your z cooordinate of point p :- ')))
# #x1,y1,z1 is coordinate points of first diagonal point.
# x1=float(input('enter your x point of one diagonal point:- '))  
# y1=float(input('enter your y point of one diagonal point:- '))
# z1=float(input('enter your z point of one diagonal point:- '))
# #x2,y2,z2 is coordinate points of another diagonal point.
# x2=float(input('enter your x point of opposite diagonal to first point:- '))
# y2=float(input('enter your y point of opposite diagonal to first point:- '))
# z2=float(input('enter your z point of opposite diagonal to first point:- '))
# #x3,y3,z3 is coordinate points of point p which we have to check.
# x3=float(input('enter your first point :- '))
# y3=float(input('enter your first point :- '))
# z3=float(input('enter your first point :- '))
# d1.x=x1
# d1.y=y1
# d1.z=z1
# d2.x=x2
# d2.y=y2
# d2.z=z2
# p.x=x3
# p.y=y3
# p.z=z3
def is_interior(d1,d2,p):
	'''
	Return True if point p is inside cuboid otherwise gives False.

	Here d1 is any point of cuboid which consist (x1,x2,x3) points and d2 is point just opposite to d1 point consisting
	of (x2,y2,z2).p is the point which we have to check either inside the cuboid or not.Here we are assuming that 
	any point on cuboid consider as inside the cuboid.

	parameter d1:takes float value of coordinates of one diagonal point from user.
	precondition:d1 value must be numeric value.

	parameter d2:takes float value of coordinates of another diagonal point opposite to first one from user.
	precondition:d2 value must be numeric value.

	parameter p:takes float value of coordinate point p from user which we have to check.
	precondition:d1 value must be numeric value.

	'''
	# return d1.x<=p.x and d2.x>=p.x and d1.y<=p.x and d2.y>=p.y and d1.z<=p.z and d2.z>=p.z
	return ((d1.x<=p.x or d1.x>=p.x)and (d2.x>=p.x or d2.x<=p.x) 
		and( d1.y<=p.x or d1.y>=p.x )and (d2.y>=p.y or d2.y<=p.y)and 
		(d1.z<=p.z or d1.z>=p.z )and (d2.z>=p.z or d2.z<=p.z))

print(is_interior(d1,d2,p))

# d1=(p1.x=x1,p1.y=y1,p1.z=z1)
# d2=(p2.x=x2,p2.y=y2,p2.z=z2)
# d3=(p3.x=x3,p3.y=y3,p3.z=z3)
"""
# x=float(input('enter your lenght'))
# y=int(input('enter your breth'))
# print(x*y)







'''
this contains a function is_interior

Author : Narayan Jat
Date:December 4,2022
'''
# Importing point module for point class
import point as t

def is_interior(d1,d2,p):
	'''
	Return : True If the point p lies inside the cuboid defined with help of d1,d2 otherwise False

	Where d1 and d2 are the diagonally opposite points of cuboid.
	If the point p is on the surface then it will be considered inside the cuboid.

	parameters d1: One point to define cuboid
	precondition : It is a point object

	parameters d2: Second point to define cuboid
	precondition : it is a point object

	parameters p: point to be checked 
	precondition :It is a point object

	Doctests:

	>>> is_interior(t.Point3(4,5,8),t.Point3(8,2,5),t.Point3(2,3,6))
	False
	>>> is_interior(t.Point3(4,5,8),t.Point3(8,2,5),t.Point3(3,3,4))
	False
	>>> is_interior(t.Point3(4,5,8),t.Point3(8,2,5),t.Point3(2,3,6))
	False
	>>> is_interior(t.Point3(4,5,8),t.Point3(8,2,5),t.Point3(2,3,9))
	False
	>>> is_interior(t.Point3(4,5,8),t.Point3(8,2,5),t.Point3(5,3,6))
	True
	'''
	if not((p.x>=d1.x or p.x>=d2.x) and (p.x<=d1.x or p.x<=d2.x)):
		return False
	elif not((p.y>=d1.y or p.y>=d2.y) and (p.y<=d1.y or p.y<=d2.y)):
		return False
	elif not((p.z>=d1.z or p.z>=d2.z) and (p.z<=d1.z or p.z<=d2.z)):
		return False
	return True
print(' 1st point cordinate for cuboid :')
d1=t.Point3(float(input('Enter x coordinate : ')),float(input('Enter y coordinate : ')),float(input('Enter z coordinate : ')))
print("2nd point coordinate for cuboid :")
d2=t.Point3(float(input('Enter x coordinate : ')),float(input('Enter y coordinate : ')),float(input('Enter z coordinate : ')))
print('coordinate of point to be checked :')
p=t.Point3(float(input('Enter x coordinate : ')),float(input('Enter y coordinate : ')),float(input('Enter z coordinate : ')))
print(is_interior(cuboid_def_p1,cuboid_def_p2,p_to_check))


def sol_is_interior(d1,d2,p):
	'''
	Return True if point p is inside cuboid otherwise gives False.

	Here d1 is any point of cuboid which consist (x1,x2,x3) points and d2 is point just opposite to d1 point consisting
	of (x2,y2,z2).p is the point which we have to check either inside the cuboid or not.Here we are assuming that 
	any point on cuboid consider as inside the cuboid.

	parameter d1:takes float value of coordinates of one diagonal point from user.
	precondition:d1 value must be numeric value.

	parameter d2:takes float value of coordinates of another diagonal point opposite to first one from user.
	precondition:d2 value must be numeric value.

	parameter p:takes float value of coordinate point p from user which we have to check.
	precondition:d1 value must be numeric value.

	'''
	return ((d1.x<=p.x or d1.x>=p.x)and (d2.x>=p.x or d2.x<=p.x) and( d1.y<=p.x or d1.y>=p.x )and (d2.y>=p.y or d2.y<=p.y)and (d1.z<=p.z or d1.z>=p.z )and (d2.z>=p.z or d2.z<=p.z))


def test_inter():
	assert is_interior(d1,d2,p)==sol_is_interior(z)