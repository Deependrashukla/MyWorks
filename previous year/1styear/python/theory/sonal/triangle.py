angle1 = float(input("Enter first angle of triangle: "))
angle2 = float(input("Enter first angle of triangle: "))
angle3 = float(input("Enter third angle of triangle: "))

#This condition checking that triangle is invalid.
if (angle1 + angle2 + angle3) > 180 or (angle1 + angle2 + angle3) < 180 or angle1 == 180 or angle2 == 180 or angle3 == 180 or angle3 == 0 or angle2 == 0 or angle3 == 0:
	print( "invalid" )

#Here we are checking that triangle is right angle triangle.			
elif angle1 == 90 or angle2 == 90 or angle3 == 90 :
	print( "right angle triangle" )

#Here we are checking that triangle is acute angle triangle.
elif angle1 < 90 and angle2 < 90 and angle3 < 90 :
	print( "acute" )	

#Here we are checking that triangle is acute obtuse triangle.	
elif angle1 > 90 or angle2 > 90 or angle3 > 90 :	
	print( "obtuse" )

