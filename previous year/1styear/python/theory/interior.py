'''
This programs tells about the point p is inside the cuboid or not.

Author: KIRTAN KHICHI
Date:December 4,2022
'''
import point
d1=point.Point3(int(input('enter your x coordinate of one diagonal point:- ')),
	float(input('enter your y point of one diagonal point:- ')),
	float(input('enter your z coordinate of one diagonal point:- ')))
d2=point.Point3(float(input('enter your x coordinate of opposite diagonal to first point:- ')),
	float(input('enter your y coordinate of opposite diagonal to first point:- ')),
	float(input('enter your z coordinate of opposite diagonal to first point:- ')))
p=point.Point3(float(input('enter your x coordinate of point p :- ')),
	float(input('enter your y coordinate point p :- ')),
	float(input('enter your z cooordinate of point p :- ')))

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
	# return ((d1.x<=p.x )and (d2.x>=p.x) and( d1.y<=p.x  )and (d2.y>=p.y )and (d1.z<=p.z  )and (d2.z>=p.z ))
	return round(d1.distance(d2)**d2.distance(p))

print(is_interior(d1,d2,p))