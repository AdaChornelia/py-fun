Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import*
>>> from random import randint
>>> import maths, os, time
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import maths, os, time
ModuleNotFoundError: No module named 'maths'
>>> import math, os, time
>>> 
>>> #initialize and setup
>>> myPen = Turtle()
>>> myPen.shape("turtle")
>>> myPen.speed(10)
>>> 
>>> window = Screen()
>>> window.title("Eid Mubarak !!")
>>> window.screensize(300,300)
>>> window.bgcolor("#072752")
>>> 
>>> 
>>> #Methods
>>> def draw_circle(paint, color, x,y, radius):
...     paint.penup()
...     paint.color(color)
...     paint.fillcolor(color)
...     paint.goto(x,y)
...     paint.pendown()
...     paint.begin_fill()
...     paint.circle(radius)
...     paint.end_fill()
... 
...     
>>> def draw_star(paint, color, x, y, size):
...     paint.penup()
...     paint.color(color)
...     paint.fillcolor(color)
...     paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    paint.right(144)
    for i in range(5):
        paint.forward(size)
        paint.right(144)
        paint.forward(size)
    paint.end_fill()
    paint.setheading(0)

    
def draw_rectangle(paint, color, x, y, width, height):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    pain.begin_fill()
    for i in range(2):
        paint.forward(width)
        paint.left(90)
        paint.forward(height)
        paint.left(90)

    
def draw_rectangle(paint, color, x, y, width, height):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    pain.begin_fill()
    for i in range(2):
        paint.forward(width)
        paint.left(90)
        paint.forward(height)
        paint.left(90)
    paint.end_fill()
    paint.setheading(0)

    
def draw_trapizium(paint, color, x,y, width, height, style):
    rad = 20*(math.pi/180) #angle in radian for calculating parallel side
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    if(style =="normal"):
        nor = 1
        rev = 0
    elif(style == "reverse"):
        nor = 0
        rev = 1

        
def draw_trapizium(paint, color, x,y, width, height, style):
    rad = 20*(math.pi/180) #angle in radian for calculating parallel side
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    if(style =="normal"):
        nor = 1
        rev = 0
    elif(style == "reverse"):
        nor = 0
        rev = 1

        
def draw_trapizium(paint, color, x,y, width, height, style):
    rad = 20*(math.pi/180) #angle in radian for calculating parallel side
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()
    if(style =="normal"):
        nor = 1
        rev = 0
    elif(style == "reverse"):
        nor = 0
        rev = 1
    paint.forward(width-rev*(2*height*math.sin(rad))) #parallel side
    paint.left(90+(20*nor)-(20*rev))
    paint.forward(height)
    paint.left(90-(20*nor)+(20*rev))
    paint.forward(width-nor*(2*height*math.sin(rad))) #parallel side
    paint.left(90-(20*nor)+(20*rev))
    paint.forward(height)
    paint.left(110+(20*nor)-(20*ref))
    paint.end_fill()
    paint.setheading(0)

    
# draw masjid
def draw_minar (paint, color, x,y):
    paint.penup()
    paint.color(color)
    paint.fillcolor(color)
    paint.goto(x,y)
    paint.pendown()
    paint.begin_fill()

    
def draw_minar (paint, color, x,y):
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
    paint.forward(7.42) #from phytagorean theorem
    #second turn
    paint.left(90)
    paint.forward(7.42)
    paint.left(45)
    paint.forward(35)
    paint.left(45)
    paint.forward(40)

    
def draw_minar (paint, color, x,y):
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
    paint.forward(7.42) #from phytagorean theorem
    #second turn
    paint.left(90)
    paint.forward(7.42)
    paint.left(45)
    paint.forward(35)
    paint.left(45)
    paint.forward(40)
    paint.end_fill()
    paint.setheading(0)

    
##########Logic
    
#draw the mesjid
    
#draw the mesjid
    
##########Logic##########
    
#draw the mesjid
    
draw_rectangle(myPen, "ffdf00", 250, -280, 50,8)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    draw_rectangle(myPen, "ffdf00", 250, -280, 50,8)
  File "<pyshell#60>", line 3, in draw_rectangle
    paint.color(color)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/turtle.py", line 2217, in color
    pcolor = self._colorstr(pcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: ffdf00
draw_rectangle(myPen, "#ffdf00", 250, -280, 50, 8)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    draw_rectangle(myPen, "#ffdf00", 250, -280, 50, 8)
  File "<pyshell#60>", line 3, in draw_rectangle
    paint.color(color)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/turtle.py", line 2217, in color
    pcolor = self._colorstr(pcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: #ffdf00
