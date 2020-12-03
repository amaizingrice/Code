import turtle
import time
from turtle import *
from random import *

#Screen setup
setup(800, 500)
title("Turtle Race")
bgcolor("green")
speed(0)

#heading
penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

#dirt
goto(-350, 200)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

#finish line
gap_size = 20
shape("square")
penup()

#white squares row 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

#white squares row 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

#black squares row 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

#black squares row 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

#Turtle- Blue
blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()

#Turtle- Purple
purple_turtle = Turtle()
purple_turtle.color("darkviolet")
purple_turtle.shape("turtle")
purple_turtle.shapesize(1.5)
purple_turtle.penup()
purple_turtle.goto(-300, 50)
purple_turtle.pendown()

#Turtle- Yellow
yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -150)
yellow_turtle.pendown()

#Turtle- Red
red_turtle = Turtle()
red_turtle.color("maroon")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5)
red_turtle.penup()
red_turtle.goto(-300, -50)
red_turtle.pendown()

#Pause 1 second before racing
time.sleep(1)

#Move the turtles
while blue_turtle.xcor() <= 230 and purple_turtle.xcor(
) <= 230 and yellow_turtle.xcor() <= 230 and red_turtle.xcor() <= 230:
    blue_turtle.forward(randint(1, 10))
    purple_turtle.forward(randint(1, 10))
    yellow_turtle.forward(randint(1, 10))
    red_turtle.forward(randint(1, 10))

    #Mark a winner
    if blue_turtle.xcor() > purple_turtle.xcor() and blue_turtle.xcor(
    ) > yellow_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor():
        print("Blue turtle wins!")

    elif purple_turtle.xcor() > blue_turtle.xcor() and purple_turtle.xcor(
    ) > yellow_turtle.xcor() and purple_turtle.xcor() > red_turtle.xcor():
        print("Purple turtle wins!")

    elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor(
    ) > purple_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor():
        print("Yellow turtle wins!")

    else:
        print("Red turtle wins!")
