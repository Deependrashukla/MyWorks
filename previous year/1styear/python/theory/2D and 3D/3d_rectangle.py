import point
print('Please ensure that coordinate are in clock wise senses ✌️')
print('Please enter one corner 1 coordinate ')
x1=int(input('enter your point x1(lower left) :- '))
y1=int(input('enter your point y1(lower left) :- '))
z1=int(input('enter your point z1(lower left) :- '))
d1=point.Point(x1,y1,z1)
print('Please enter one corner 2 coordinate ')
x2=int(input('enter your point x2(upper left) :- '))
y2=int(input('enter your point y2(upper left) :- '))
z2=int(input('enter your point z2(lower left) :- '))
d2=point.Point(x2,y2,z2)
print('Please enter one corner 3 coordinate ')
x3=int(input('enter your point x3(upper right) :- '))
y3=int(input('enter your point y3(upper right) :- '))
z3=int(input('enter your point z3(lower left) :- '))
d3=point.Point(x3,y3,z3)
print('Please enter one corner 4 coordinate ')
x4=int(input('enter your point x4(lower right) :- '))
y4=int(input('enter your point y4(lower right) :- '))
z4=int(input('enter your point z4(lower left) :- '))
d4=point.Point(x4,y4,z4)
print('Point which you have to check ')
x=int(input('enter your point x :- '))
y=int(input('enter your point y :- '))
z=int(input('enter your point z :- '))
p=point.Point(x,y,z)

def is_interior():

	if x1==x2==x3==x4==y1==y2==y3==y4==z1==z2==z3==z4 :
		print('Please Enter correct coordinates all coordinates are same ! 😁😁')
	elif (((x4-x3)**2 + (y4-y3)**2 +(z4-z3)**2)**0.5) == (((x2-x1)**2 + (y2-y1)**2 +(z2-z1)**2)**0.5)and(((x2-x3)**2 + (y2-y3)**2 +(z2-z3)**2)**0.5) == (((x4-x1)**2 + (y4-y1)**2 +(z4-z1)**2)**0.5)and((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2) == ((x4-x2)**2 + (y4-y2)**2 +(z4-z2)**2):
		if distance()
	else:
		print('Your coordinate not forming a rect angle 😔')