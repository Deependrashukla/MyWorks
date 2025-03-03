# x1=input('Enter your x coardinate of p1:')
# y1=input('Enter your y coardinate of p1:')
# x2=input('Enter your x coardinate of p2:')
# y2=input('Enter your y coardinate of p2:')
# x3=input('enter your x coardinate of p3:')
# y3=input('Enter your y coardinate of p3:')
# x4=input('Enter your x coardinate of p4:')
# y4=input('Enter your y coardinate of p4:')
# x5=input('Enter your x coardinate of p5(to check):')
# y5=input('Enter your y coardinate of p5(to check):')
x5=int(input('enter your point x :- '))
y5=int(input('enter your point y :- '))
x1=-2
y1=0
x2=-2
y2=-2
x3=2
y3=-2
x4=2
y4=0
a=slope_1(p1,p2)
b=slope_2(p2,p3)
c=slope_3(p3,p4)
d=slope_4(p4,p1)
p1=(x1,y1)
p2=(x2,y2)
p3=(x3,y3)
p4=(x4,y4)
p5=(x5,y5)
if (int(x2)-int(x1))==0 or (int(x3)-int(x2))==0 or (int(x4)-int(x3))==0 or (int(x1)-int(x4))==0:
	if (int(x1)==int(x4) and int(x2)==int(x3) and int(y1)==int(y2) and int(y3)==int(y4)) or (int(x1)==int(x2) and int(x3)==int(x4) and int(y1)==int(y4) and int(y2)==int(y3)):
		if (int(x1)==int(x2)==int(x3)==int(x4)) or (int(y1)==int(y2)==int(y3)==int(y4)) or (int(x1)==int(x4) and int(x2)==int(x3) and int(y1)==int(y4) and int(y2)==int(y3)):
			print("points not forming rectangle")
		elif 
		else:
			if ((int(x1)<int(x5)<int(x4)) or (int(x4)<int(x5)<int(x1)) and ((int(y1)<int(y5)<int(y2)) or (int(y2)<int(y5)<int(y1)))) or ((int(x1)<int(x5)<int(x2)) or (int(x2)<int(x5)<int(x1)) and ((int(y3)<int(y5)<int(y2)) or (int(y2)<int(y5)<int(y3)))):
				print("POints inside the rectangle")
			else:
				print("Outside the rectangle")
	else:
		print("Points not forming rectangle")
else:
	def slope_1(p1,p2):
		s1=(int(y2)-int(y1))/(int(x2)-int(x1))
		return s1
	def slope_2(p2,p3):
		s2=(int(y3)-int(y2))/(int(x3)-int(x2))
		return s2
	def slope_3(p3,p4):
		s3=(int(y4)-int(y3))/(int(x4)-int(x3))
		return s3
	def slope_4(p4,p1):
		s4=(int(y1)-int(y4))/(int(x1)-int(x4))
		return s4
	a=slope_1(p1,p2)
	b=slope_2(p2,p3)
	c=slope_3(p3,p4)
	d=slope_4(p4,p1)
	if a==c and b==d and a*b==-1:
		print('Great it forms a rectangle')
		if ((int(y4)-int(y1))-((a)*(int(x4)-int(x1))))*((int(y5)-int(y1))-((a)*(int(x5)-int(x1))))>0 and (((int(y1)-int(y2))-(b)*(int(x1)-int(x2))))*((int(y5)-int(y2))-(b)*(int(x5)-int(x2)))>0 and (((int(y2)-int(y3))-(c)*(int(x2)-int(x3))))*((int(y5)-int(y3))-(c)*(int(x5)-int(x3)))>0 and (((int(y3)-int(y4))-(d)*(int(x3)-int(x4))))*((int(y5)-int(y4))-(d)*(int(x5)-int(x4)))>0:
			print("Your point is inside the rectangle")
		else:
			print("Your point is outside the rectangle")
	else:
		print("Points does not forms a rectangle")















