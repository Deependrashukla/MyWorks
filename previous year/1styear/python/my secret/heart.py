import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(10)
t.color("red")

# Draw the heart shape
t.begin_fill()
t.left(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

# Hide the turtle when we're done
t.hideturtle()
