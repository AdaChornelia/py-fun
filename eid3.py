import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("#0a043c")
screen.title("Eid Mubarak")

# Set up the turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.setposition(0, -200)
pen.pendown()

# Draw the base of the mosque
pen.color("#f8dbba")
pen.begin_fill()
pen.forward(300)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(600)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(300)
pen.end_fill()

# Draw the dome of the mosque
pen.penup()
pen.setposition(0, 100)
pen.pendown()
pen.color("#c79a6b")
pen.begin_fill()
pen.circle(150)
pen.end_fill()

# Draw the minaret of the mosque
pen.penup()
pen.setposition(-120, 100)
pen.pendown()
pen.color("#f5f5f5")
pen.begin_fill()
pen.forward(60)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(200)
pen.end_fill()

# Draw the crescent moon on top of the dome
pen.penup()
pen.setposition(0, 250)
pen.pendown()
pen.color("#f5f5f5")
pen.begin_fill()
pen.circle(50, -180)
pen.end_fill()

# Write the message "Eid Mubarak" below the mosque
pen.penup()
pen.setposition(0, -300)
pen.pendown()
pen.color("#f5f5f5")
pen.write("Eid Mubarak", align="center", font=("Arial", 36, "bold"))

# Hide the turtle pen
pen.hideturtle()

# Keep the turtle screen open until closed by the user
turtle.done()
