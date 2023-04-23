# importing the turtle module
from turtle import *

# making an example for drawing
ttl = turtle.Turtle()    

# create screen to draw
screen = turtle.Screen()

# setting the screen size
screen.setup(400,500)

# set background as white
screen.bgcolor('navy')

# set the color of the pen
ttl.pencolor('light blue')

# set the size of the pen
ttl.pensize(6)

# setting the speed of drawing with the pen
ttl.speed(1.2)

#set the shape of the pen as Turtle
ttl.shape('turtle')

##############done for main part of the animation

# printing the heading on the screen

ttl.penup()
ttl.setpos(-100,90)
ttl.pendown()

# set the pen color
ttl.pencolor('white')
ttl.write('Square Animation', font = ("Arial", 20, "bold"))
ttl.penup
ttl.ht()

#starting to draw the square
ttl.forward(120)    #top (first) side
ttl.right(90)
ttl.forward(120)    # right (second) side
ttl.right(90)
ttl.forward(120)   # bottom (third) side
ttl.right(90)
ttl.forward(120)   # left (fourth) side

# Printing the heading on the screen
ttl.penup()
ttl.setpos(-100,90)
ttl.pendown()
ttl.pencolor('white')
ttl.write('Square Animation', font=("Arial", 20, "bold"))
ttl.penup()
ttl.ht()
