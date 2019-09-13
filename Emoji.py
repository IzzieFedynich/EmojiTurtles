import turtle
from turtle import Turtle



Raphael: Turtle = turtle.Turtle()
Michelangelo = turtle.Turtle()
Donatello = turtle.Turtle()
Leonardo = turtle.Turtle()

Raphael.shape("turtle")
Michelangelo.shape("turtle")
Donatello.shape("turtle")
Leonardo.shape("turtle")
turtle.bgcolor("pale turquoise")

Raphael.speed(12)
Michelangelo.speed(10)

Raphael.turtlesize(.1)
Michelangelo.turtlesize(.1)
Donatello.turtlesize(.1)
Leonardo.turtlesize(.1)

Raphael.fillcolor("gold")
Raphael.begin_fill()
Raphael.circle(120)
Raphael.end_fill()
Raphael.color("gold")


Michelangelo.fillcolor("goldenrod")
Michelangelo.begin_fill()
Michelangelo.penup()
Michelangelo.goto(-80,100)
Michelangelo.pendown()
Michelangelo.right(90)
Michelangelo.circle(80,180)
Michelangelo.right(90)
Michelangelo.backward(160)
Michelangelo.end_fill()
Michelangelo.color("goldenrod")



Donatello.penup()
Donatello.fillcolor("goldenrod")
Donatello.begin_fill()
Donatello.goto(-50,150)
Donatello.pendown()
Donatello.circle(15)
Donatello.end_fill()
Donatello.color("goldenrod")



Leonardo.fillcolor("goldenrod")
Leonardo.begin_fill()
Leonardo.penup()
Leonardo.goto(50,150)
Leonardo.pendown()
Leonardo.circle(15)
Leonardo.end_fill()
Leonardo.color("goldenrod")

turtle.exitonclick()
