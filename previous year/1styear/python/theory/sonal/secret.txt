'''
author : sonal kumari.
'''
import turtle
sonal=turtle.Turtle()
sonal.width(8)
sonal.color("#00FF00")
new=turtle.getscreen()
sonal.speed(10)

new.bgcolor("lightblue")

# Hidden Work(penup)
sonal.left(180)
sonal.penup()
sonal.forward(300)
sonal.right(90)
sonal.forward(100)
sonal.pendown()

# Printing H

#start to draw
sonal.forward(50)
sonal.right(90)
sonal.forward(50)
sonal.left(90)
sonal.forward(50)
sonal.left(90)

sonal.penup()
sonal.forward(50)
sonal.left(90)
sonal.pendown()
sonal.forward(50)
sonal.left(90)
sonal.forward(50)
sonal.right(90)
sonal.forward(50)


# printing A

sonal.penup()
sonal.left(90)
sonal.forward(15)
sonal.pendown()
sonal.left(70)
sonal.forward(110)
sonal.right(70)
sonal.right(70)
sonal.forward(110)
sonal.left(180)
sonal.forward(55)
sonal.left(70)
sonal.forward(38)
sonal.left(70)
sonal.penup()
sonal.forward(55)
sonal.left(110)

sonal.forward(100)

# printing P

sonal.left(90)
sonal.pendown()
sonal.forward(100)
sonal.right(90)
sonal.forward(50)
sonal.right(20)
sonal.forward(20)
sonal.right(70)
sonal.forward(40)
sonal.right(70)
sonal.forward(20)
sonal.right(20)
sonal.forward(50)
sonal.left(90)
sonal.forward(50)
sonal.left(90)
sonal.penup()
sonal.forward(100)


# printing P

sonal.left(90)
sonal.pendown()
sonal.forward(100)
sonal.right(90)
sonal.forward(50)
sonal.right(20)
sonal.forward(20)
sonal.right(70)
sonal.forward(40)
sonal.right(70)
sonal.forward(20)
sonal.right(20)
sonal.forward(50)
sonal.left(90)
sonal.forward(50)
sonal.left(90)
sonal.penup()
sonal.forward(100)

# printing Y

sonal.forward(20)
sonal.pendown()
sonal.left(90)
sonal.forward(50)
sonal.left(30)
sonal.forward(60)
sonal.backward(60)
sonal.right(60)
sonal.forward(60)
sonal.backward(60)
sonal.left(30)

# go to Home

sonal.penup()
sonal.home()

sonal.color("orange")
new.bgcolor("white")
# setting second row

sonal.backward(300)
sonal.right(90)
sonal.forward(60)
sonal.left(180)


# printing P


sonal.pendown()
sonal.forward(100)
sonal.right(90)
sonal.forward(50)
sonal.right(20)
sonal.forward(20)
sonal.right(70)
sonal.forward(40)
sonal.right(70)
sonal.forward(20)
sonal.right(20)
sonal.forward(50)
sonal.backward(50)
sonal.left(180)
sonal.right(20)
sonal.forward(20)
sonal.right(70)
sonal.forward(40)
sonal.right(70)
sonal.forward(20)
sonal.right(20)
sonal.forward(50)
sonal.right(90)
sonal.forward(10)


# go to Home

sonal.penup()
sonal.home()

# setting up

sonal.backward(200)
sonal.right(90)
sonal.forward(10)
sonal.left(90)
sonal.pendown()
sonal.forward(20)
sonal.penup()
sonal.home()

# D

sonal.backward(150)
sonal.right(90)
sonal.forward(60)
sonal.pendown()
sonal.backward(100)
sonal.right(90)
sonal.forward(10)
sonal.backward(70)
sonal.left(180)
sonal.right(20)
sonal.forward(20)
sonal.right(70)
sonal.forward(88)
sonal.right(70)
sonal.forward(20)
sonal.right(20)
sonal.forward(70)

sonal.penup()
sonal.home()

# set up for A

sonal.backward(50)
sonal.right(90)
sonal.forward(65)
sonal.left(90)



# printing A


sonal.pendown()
sonal.left(70)
sonal.forward(110)
sonal.right(70)
sonal.right(70)
sonal.forward(110)
sonal.left(180)
sonal.forward(55)
sonal.left(70)
sonal.forward(38)
sonal.left(70)
sonal.penup()
sonal.forward(55)
sonal.left(110)

sonal.forward(100)

# printing Y


sonal.pendown()
sonal.left(90)
sonal.forward(50)
sonal.left(30)
sonal.forward(60)
sonal.backward(60)
sonal.right(60)
sonal.forward(60)
sonal.backward(60)
sonal.left(30)

# go to Home

sonal.penup()
sonal.home()


# settig pogition

sonal.right(90)
sonal.forward(215)
sonal.right(90)
sonal.forward(200)
sonal.right(90)

#color

sonal.color("blue")
new.bgcolor("black")

# setup
sonal.penup()
sonal.left(90)
sonal.forward(80)
sonal.left(90)
sonal.forward(7)


sonal.forward(100)

# design


#design pattern
sonal.home()
sonal.forward(200)
sonal.pendown()
sonal.color("PURPLE")
sonal.width(3)
sonal.speed(0)

def squre(length, angle):

    sonal.forward(length)
    sonal.right(angle)
    sonal.forward(length)
    sonal.right(angle)

    sonal.forward(length)
    sonal.right(angle)
    sonal.forward(length)
    sonal.right(angle)

squre(80, 90)

for i in range(36):
      sonal.right(10)
      squre(80, 90)




turtle.mainloop()