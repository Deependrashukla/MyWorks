print('Please ensure that coordinate are in clock wise senses ✌️')
print('Please enter one corner 1 coordinate ')
x1=int(input('enter your point x1(lower left) :- '))
y1=int(input('enter your point y1(lower left) :- '))
print('Please enter one corner 2 coordinate ')
x2=int(input('enter your point x2(upper left) :- '))
y2=int(input('enter your point y2(upper left) :- '))
print('Please enter one corner 3 coordinate ')
x3=int(input('enter your point x3(upper right) :- '))
y3=int(input('enter your point y3(upper right) :- '))
print('Please enter one corner 4 coordinate ')
x4=int(input('enter your point x4(lower right) :- '))
y4=int(input('enter your point y4(lower right) :- '))
print('Point which you have to check ')
x=int(input('enter your point x :- '))
y=int(input('enter your point y :- '))
if x1==x2==x3==x4==y1==y2==y3==y4 :
	print('PLease Enter correct coordinates all coordinates are same ! 😁😁')
elif (((x4-x3)**2 + (y4-y3)**2)**0.5) == (((x2-x1)**2 + (y2-y1)**2)**0.5)and(((x2-x3)**2 + (y2-y3)**2)**0.5) == (((x4-x1)**2 + (y4-y1)**2)**0.5):
	if ((y-y4)*(x4-x1)-(y4-y1)*(x-x4) )>=0 and ((y-y3)*(x4-x3)-(x-x3)*(y4-y3))<=0 and ((y-y2)*(x3-x2)-(x-x2)*(y3-y2))<=0 and ((y-y1)*(x2-x1)-(x-x1)*(y2-y1))<=0 :
		print('point inside the rectangle 👍') 
	else:
		print('point outside the rectangle 👎')
else:
	print('Your coordinate not forming a rect angle 😔')
