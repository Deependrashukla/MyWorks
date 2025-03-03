import math
A=float(input("enter A:"))
B=float(input("enter B:"))
C=float(input("enter C:"))
x0=float(input("enter x0:"))
v0=float(input("enter v0:"))


alpha=-B/(2*A)
bita=abs(((B**2/4)-C/A)**1/2)
lambda1=(-B-(B*2-4*A*C)*0.5)/2*A
lambda2=(-B+(B*2-4*A*C)*0.5)/2*A
lambda3=-B/(2*A)
if lambda1 != lambda2 :


	d1=(v0-lambda2*x0)/(lambda1-lambda2)
	d2=(v0-lambda1*x0)/(lambda2-lambda1)
t=0
t1=[0.0,1.0,2.0,3.0,4.0,5.0]
x1=[]

	
def over_damped():
	global x,t
	for i in t1:
		t=i
		x=d1*math.exp(lambda1*t)+d2*math.exp(lambda2*t)
		x1.append(x)
	return x1
	
def critically_damped():
	global x,t
	for i in t1:
		t=i
		x=(x0+(v0-lambda3*x0)*t)*math.exp(lambda1*t)
		x1.append(x)
	return x1	


def under_damped():
	global x,t
	for i in t1:
		t=i
		x=math.exp(alpha*t)*(x0*math.cos(bita*t))+((v0+alpha*x0)*math.sin(bita*t))/bita
		x1.append(x)
	return x1


def about_damped():
	if B**2-4*A*C > 0:
		print("over damped")
		return over_damped()
	elif B**2-4*A*C == 0:
		print("critically damped")
		return critically_damped()
	elif B**2-4*A*C < 0:
		print("under damped")
		return under_damped()

print(about_damped())


import plotly.express as px
fig=px.line(x = t1, y = x1)
fig.show()

