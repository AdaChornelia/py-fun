import turtle

# Set up the turtle window
wn = turtle.Screen()
wn.bgcolor("#222222")

# Create a turtle for the greeting text
greeting = turtle.Turtle()
greeting.speed(0)
greeting.color("#ffffff")
greeting.penup()
greeting.goto(0, 100)
greeting.write("Eid Mubarak!", align="center", font=("Arial", 40, "bold"))

# Create a turtle for the mosques
mosque1 = turtle.Turtle()
mosque1.speed(0)
mosque1.color("#ffffff")
mosque1.penup()
mosque1.goto(-200, -100)
mosque1.pendown()
for i in range(4):
    mosque1.forward(100)
    mosque1.left(90)
mosque1.forward(50)
mosque1.left(120)
mosque1.forward(50)
mosque1.left(120)
mosque1.forward(50)
mosque1.penup()

mosque2 = turtle.Turtle()
mosque2.speed(0)
mosque2.color("#ffffff")
mosque2.penup()
mosque2.goto(200, -100)
mosque2.pendown()
for i in range(4):
    mosque2.forward(100)
    mosque2.left(90)
mosque2.forward(50)
mosque2.left(120)
mosque2.forward(50)
mosque2.left(120)
mosque2.forward(50)
mosque2.penup()

# Create a turtle for the moon and stars
moon = turtle.Turtle()
moon.speed(0)
moon.color("#f2c744")
moon.penup()
moon.goto(-300, 200)
moon.pendown()
moon.begin_fill()
moon.circle(50)
moon.end_fill()

star1 = turtle.Turtle()
star1.speed(0)
star1.color("#f2c744")
star1.penup()
star1.goto(-270, 230)
star1.pendown()
for i in range(5):
    star1.forward(20)
    star1.right(144)

star2 = turtle.Turtle()
star2.speed(0)
star2.color("#f2c744")
star2.penup()
star2.goto(-320, 170)
star2.pendown()
for i in range(5):
    star2.forward(20)
    star2.right(144)

star3 = turtle.Turtle()
star3.speed(0)
star3.color("#f2c744")
star3.penup()
star3.goto(-240, 170)
star3.pendown()
for i in range(5):
    star3.forward(20)
    star3.right(144)

# Animate the greeting text and the moon and stars
for i in range(50):
    greeting.shapesize(1+i/10)
    moon.goto(moon.xcor()+10, moon.ycor()-5)
    star1.goto(star1.xcor()+10, star1.ycor()-5)
    star2.goto(star2.xcor()+10, star2.ycor()-5)
    star3.goto(star3.xcor()+10, star3.ycor()-5)
