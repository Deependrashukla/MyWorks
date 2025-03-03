# list1=[int(input('enter your point x1 : ')),int(input('enter your point y1(lower left) :- ')),int(input('enter your point x2 : ')),int(input('enter your point y2 : ')),int(input('enter your point x3 : ')),int(input('enter your point y3 : ')),int(input('enter your point x4 : ')),int(input('enter your point y4 : '))]
print('Please enter one corner 1 coordinate ')
x1=int(input('enter your point x1 : '))
y1=int(input('enter your point y1 : '))
print('Please enter one corner 2 coordinate ')
x2=int(input('enter your point x2 : '))
y2=int(input('enter your point y2 : '))
print('Please enter one corner 3 coordinate ')
x3=int(input('enter your point x3 : '))
y3=int(input('enter your point y3 : '))
print('Please enter one corner 4 coordinate ')
x4=int(input('enter your point x4 : '))
y4=int(input('enter your point y4 : '))

def is_rectangle():
	'''
	This function tells us that our rectangle will exists or not on given points.

	Here we are taking values from user and give the output on the basis of user input like
	i.e rectangle is not forms or if rectangle exits then call another function point checking().

	'''
	#This line checking that rectangle is parallel to x-axis or not.
	if (x2-x1)==0 or (x4-x1)==0 or (x2-x3)==0 or (x3-x4)==0:
		# This also checking that rectangle is parallel or not to x-axis.
		if ((x1==x2 and x3==x4) and (y1==y4 and y3==y2) or (x1==x4 and x2==x3) and (y1==y2 and y3==y4)):
			#some special cases when rectangle will not forms.
			if (x1==x2==x3==x4) or (y1==y2==y3==y4) or (x1==x4 and x2==x3 and y1==y4 and y2==y3) :
				print('Your coordinate not forming a rect angle 😔')

			
			else:
				print('Point which you have to check ')
				global x,y
				x=int(input('enter your point x : '))
				y=int(input('enter your point y : '))
				# If rectangle is parallel to x=axis then rect_parallel() will run.
				rect_parallel()
		else:
			print('Your coordinate not forming a rect angle 😔')
	else:
		rect_inclined()



def slope(w,x,y,z):
	'''
	Returns the slope of according to points of the line.

	Parameter w:take value from user.
	Precondition:Value must be numeric real number.

	Parameter x:Takes value from user.
	Precondition:Value must be numeric real number

	Parameter y:Takes value from user.
	Precondition:Value must be numeric real number

	Parameter z:Takes value from user.
	Precondition:Value must be numeric real number

	'''
	return (z-y)/(x-w)

#rect_parallel() only work for rectangle which have zero slope from x-axis or infinity from x-axis.
def rect_parallel():
	'''
	Here we checking that point inside ,outside or above the rectangle.(only for Rect angle which is parallel to x axis.)

	'''
	#Here we are checking that point is on rectangle.
	if ((y-y4)*(x4-x1)-(y4-y1)*(x-x4))==0 or ((y-y3)*(x4-x3)-(x-x3)*(y4-y3))==0 or ((y-y2)*(x3-x2)-(x-x2)*(y3-y2))==0 or ((y-y1)*(x2-x1)-(x-x1)*(y2-y1))==0:
		print('Your point is on the rectangle 😁')
	#Here we are checking that point inside.
	elif ((x1<=x<=x2 or x2<=x<=x1) and (y2<=y<=y3 or y3<=y<=y2)) or ((x1<=x<=x4 or x4<=x<=x1) and (y1<=y<=y2 or y2<=y<=y1)) :
		print('point inside the rectangle 👍')
	#Here we are checking that point ouside
	else:
		print('point outside the rectangle 👎')

#rect_incilned() function runs when slope is not infinity.
def rect_inclined():
	'''
	Here we checking that point inside,outside or above the rectangle.(for inclined rectangle.)

	'''
	a=slope(x1,x2,y1,y2)  #Here we taking slope of straight line.
	b=slope(x2,x3,y2,y3)  #Here we taking slope of straight line.
	c=slope(x3,x4,y3,y4)  #Here we taking slope of straight line.
	d=slope(x1,x4,y1,y4)  #Here we taking slope of straight line.
	# Here we are checking that rectangle exits or not.
	print('Point which you have to check ')
	x=int(input('enter your point x :- '))
	y=int(input('enter your point y :- '))
	if a==c and b==d and a*b==-1:
		#Here we are checking that point inside.
		if ((y4-y1)-a*(x4-x1))*((y-y1)-a*(x-x1))>0 and ((y1-y2)-b*(x1-x2))*((y-y2)-b*(x-x2))>0 and ((y2-y3)-c*(x2-x3))*((y-y3)-c*(x-x3))>0 and ((y3-y4)-d*(x3-x4))*((y-y4)-d*(x-x4))>0 :
			print('point inside the rectangle 👍')
		#Here we are checking that point on the rectangle.
		elif ((y-y4)*(x4-x1)-(y4-y1)*(x-x4))==0 or ((y-y3)*(x4-x3)-(x-x3)*(y4-y3))==0 or ((y-y2)*(x3-x2)-(x-x2)*(y3-y2))==0 or ((y-y1)*(x2-x1)-(x-x1)*(y2-y1))==0:
			print('Your point is on the rectangle 😁')
		else:
			#Here we are checking that point outside.
			print('point outside the rectangle 👎')
	else:
		print('Your coordinate not forming a rect angle 😔')
is_rectangle()