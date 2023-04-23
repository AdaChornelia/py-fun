
from turtle import *
from random import randint
import math, os, time

#initialize and setup
myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = Screen()
window.title("Eid Mubarak!")
window.screensize(300,300)
window.bgcolor("#072752")


#Methods
def draw_circle(paint, color, x,y, radius):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    paint.circle(radius)
    paint.end_fill()

def draw_star(paint,color,x,y,size):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    paint.right(144)
    for i in range(5):
        paint.forward(size)
        paint.right(144)
        paint.forward(size)
    paint.end_fill()
    paint.setheading(0)


def draw_rectangle(paint,color,x,y,width,height):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    for i in range(2):
        paint.forward(width)
        paint.left(90)
        paint.forward(height)
        paint.left(90)

    paint.end_fill()
    paint.setheading()


def draw_trapezium(paint,color,x,y,width,height,style):
    rad = 20*(math.pi/180) #angle in radiant for calculation parallel side
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()

    if(style == "normal"):
        nor = 1
        rev = 0
    elif(style == "reverse"):
        nor = 1
        rev = 0

    paint.forward(width - rev*(2*heigh*math.sin(rad))) #parallel side
    paint.left(90+(20*nor)+(20*ref))
    paint.forward(height)
    paint.left(90-(20*nor)+(20*rev))
    paint.forward(width - nor * (2*heigh*math.sin(rad))) #parallel side
    paint.left(90 - (20*nor)+(20*rev))
    paint.forward(height)
    paint.left(110 + (20*nor)-(20*rev))

    paint.end_fill()
    paint.setheading()


#draw mesjid
def draw_minar(paint,color,x,y):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()

    #first turn
    paint.forward(60)
    paint.left(90)
    paint.forward(40)
    paint.left(45)
    paint.forward(35)
    paint.right(45)
    paint.forward(30)
    paint.left(45)
    paint.forward(7.42) #from phytagoras theorem


    #second turn
    paint.left(90)
    paint.forward(7.42)
    paint.left(45)
    paint.forward(30)
    paint.right(45)
    paint.forward(35)
    paint.left(45)
    paint.forward(40)

    paint.end_fill()
    paint.setheading(0)



####################Logic#########################
#draw the minar
draw_rectangle(myPen, "#ffdf00",250,-280,50,8)
draw_trapezium(myPen, "white", 245,-265,60,12,"normal")

draw_rectangle(myPen, "#ffa500", 250, -245, 10,70)
draw_rectangle(myPen, "#ffc500", 267, -245, 16,70)
draw_rectangle(myPen, "#ffa500", 290, -245, 10,70)

draw_trapezium(myPen, "white", 250, -168, 60, 12, "reverse")

draw_rectangle(myPen, "white", 233, -145, 10,20)
draw_rectangle(myPen, "white", 245, -145, 60,20)
draw_rectangle(myPen, "white", 307, -145, 10,20)

draw_trapezium(myPen, "#ffa500", 238, -115, 75, 18, "normal")
draw_rectangle(myPen, "#ffdf00", 245, -90, 60,15)

draw_minar(myPen, "#6799ff", 245,-65)

#draw the moon
draw_circle(myPen, "white", 210, -10,30)
draw_circle(myPen, "#072752", 203, -3, 30)

#draw the stars
draw_star(myPen, "white", 280,70,13)
for i in range(1,18):
    x = randint(-220,215)
    y = randint(-72,270)
    size = randint(8,15)
    draw_star(myPen, "white", x,y,size)


#text
myPen.penup()
myPen.setposition(-85,-140)
image_name = "./images/eid.gif"
#add the shape
window.addshape(os.path.join(os.path.dirname(__file__), image_name))
myPen.shape(os.path.join(os.path.dirname(__file__),image_name))
myPen.stamp()

myPen.color("white")
myPen.goto(-80,-240)
myPen.write("Eid Mubarak", True, "center", ("Gabriola", 38, ("bold", "italic")))

myPen.penup()
