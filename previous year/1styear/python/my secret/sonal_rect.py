x=int(input('enter your pt 1 x axis :-'))
y=int(input('enter your pt 1 y axis :-'))
def rectangle():
	x1=int(input("enter ur len1:"))
	y1=int(input("enter ur len1:"))
	x2=int(input("enter ur len2:"))
	y2=int(input("enter ur len2:"))
	x3=int(input("enter ur len3:"))
	y3=int(input("enter ur len3:"))
	x4=int(input("enter ur len4:"))
	y4=int(input("enter ur len4:"))
	if ((y-y4)*(x4-x1)-(y4-y1)*(x-x4))>=0:
		if ((y-y3)*(x4-x3)-(x-x3)*(y4-y3))<=0:
			if ((y-y2)*(x3-x2)-(x-x2)*(y3-y2))<=0:
				if ((y-y1)*(x2-x1)-(x-x1)*(y2-y1))<=0:
					return True
	else:
		return False
print(rectangle())