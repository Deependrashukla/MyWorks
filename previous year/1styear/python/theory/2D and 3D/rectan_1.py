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
x=int(input('enter your point x : '))
y=int(input('enter your point y : '))
def is_interior(x,y):
	if x1==x4 and x2==x3 and y1==y2 and y4==y3:
		if (x1<=x<=x2 or x2<=x<=x1) and y1<=y<=y4 or (y4<=y<=y1):
			print('the point is inside')
		else:print('the point is not inside rectangle ')
	elif (y2-y1/x2-x1)*(x-x1)-(y-y1)<0 and (y3-y2/x3-x2)*(x-x2)-(y-y2)<0 and (y4-y3/x4-x3)*(x-x3)-(y-y3)>0 and (y4-y1/x4-x1)*(x-x4)-(y-y4)>0:
		print('the point is inside')
def rectangle():
	if ((x1==x2 and x3==x4) and (y1==y2 and y3==y4) or (x1==x4 and x2==x3) and (y1==y4 and y2==y3)):
		print('Your coordinate not forming a rect angle 😔.')
	elif (x1==x2==x3==x4) or (y1==y2==y3==y4) or (x1==x4 and x2==x3 and y1==y4 and y2==y3) :
		print('Your coordinate not forming a rect angle 😔')
		# quit()
	elif (x1-x2)**2+(y1-y2)**2==(x4-x3)**2+(y4-y3)**2 and (x1-x4)**2+(y1-y4)**2==(x3-x2)**2+(y3-y2)**2 and (x1-x3)**2+(y3-y1)**2==(x4-x2)**2+(y4-y2)**2:
		if (x1+x3)==(x2+x4) and (y2+y4)==(y1+y3):
			if (x1-x2)**2+(y1-y2)**2+(x2-x3)**2+(y2-y3)**2+(x1-x3)**2+(y1-y3)**2==(x1-x3)**2+(y1-y2)**2+(x3-x4)**2+(y1-y4)**2+(x4-x1)**2+(y4-y1)**2:
				print('it is rectangle')
				is_interior(x,y)
			else:print('not rectangle')
		else:print('not rectangle')		
	else:print('not rectangle')	
rectangle()