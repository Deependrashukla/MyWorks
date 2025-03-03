# print('Please ensure that coordinate are in clock wise senses ✌️')
# print('Please enter one corner 1 coordinate ')
# x1=int(input('enter your point x1(lower left) :- '))
# y1=int(input('enter your point y1(lower left) :- '))
# print('Please enter one corner 2 coordinate ')
# x2=int(input('enter your point x2(upper left) :- '))
# y2=int(input('enter your point y2(upper left) :- '))
# print('Please enter one corner 3 coordinate ')
# x3=int(input('enter your point x3(upper right) :- '))
# y3=int(input('enter your point y3(upper right) :- '))
# print('Please enter one corner 4 coordinate ')
# x4=int(input('enter your point x4(lower right) :- '))
# y4=int(input('enter your point y4(lower right) :- '))
# print('Point which you have to check ')
# x=int(input('enter your point x :- '))
# y=int(input('enter your point y :- '))
# if x1==x2==x3==x4==y1==y2==y3==y4 or x1==x2==x3==x4 or y1==y2==y3==y4:
# 	print('Please Enter correct coordinates coordinates are same ! 😁😁')
# elif (((x4-x3)**2 + (y4-y3)**2)**0.5) == (((x2-x1)**2 + (y2-y1)**2)**0.5)and(((x2-x3)**2 + (y2-y3)**2)**0.5) == (((x4-x1)**2 + (y4-y1)**2)**0.5)and((x3-x1)**2 + (y3-y1)**2) == ((x4-x2)**2 + (y4-y2)**2):
# 	if ((y-y4)*(x4-x1)-(y4-y1)*(x-x4) )>=0 and ((y-y3)*(x4-x3)-(x-x3)*(y4-y3))<=0 and ((y-y2)*(x3-x2)-(x-x2)*(y3-y2))<=0 and ((y-y1)*(x2-x1)-(x-x1)*(y2-y1))<=0 :
# 		print('point inside the rectangle 👍') 
# 	else:
# 		print('point outside the rectangle 👎')
# else:
# 	print('Your coordinate not forming a rect angle 😔')

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
if (x2-x1)==0 or (x4-x1)==0 or (x2-x3)==0 or (x3-x4)==0:
	if ((x1==x2 and x3==x4) and (y1==y4 and y3==y2) or (x1==x4 and x2==x3) and (y1==y2 and y3==y4)):
		if (x1==x2==x3==x4) or (y1==y2==y3==y4) or (x1==x4 and x2==x3 and y1==y4 and y2==y3) :
			print('Your coordinate not forming a rect angle 😔')
		else:
			if ((x1<x<x2 or x2<x<x1) and (y1<y<y4 or y4<y<y1) and (y1<y<y2 or y2<y<y1) )or (x1<x<x4 or x4<x<x1) and (y1<y<y4 or y4<y<y1) and (y2<y<y3 or y3<y<y2):
				print('point inside the rectangle 👍')	 
			else:
				print('point outside the rectangle 👎')
	else:
		print('Your coordinate not forming a rect angle 😔')
else:
	def slope(w,x,y,z):
		return (z-y)/(x-w)
	a=slope(x1,x2,y1,y2)
	b=slope(x2,x3,y2,y3)
	c=slope(x3,x4,y3,y4)
	d=slope(x1,x4,y1,y4)
	if a==c and b==d and a*b==-1:
		if ((y4-y1)-a*(x4-x1))*((y-y1)-a*(x-x1))>=0 and ((y1-y2)-b*(x1-x2))*((y-y2)-b*(x-x2))>=0 and ((y2-y3)-c*(x2-x3))*((y-y3)-c*(x-x3))>=0 and ((y3-y4)-d*(x3-x4))*((y-y4)-d*(x-x4))>=0 :
			print('point inside the rectangle 👍')
		else:
			print('point outside the rectangle 👎')
	else:
		print('Your coordinate not forming a rect angle 😔')
