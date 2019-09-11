import turtle
from turtle import Turtle

Raphael: Turtle = turtle.Turtle()
Michelangelo = turtle.Turtle()
Donatello = turtle.Turtle()
Leonardo = turtle.Turtle()
scn = turtle.Screen()

Raphael.shape("turtle")
Michelangelo.shape("turtle")
Donatello.shape("turtle")
Leonardo.shape("turtle")
turtle.bgcolor("pale turquoise")



Raphael.begin_fill()
Raphael.circle(120, 180)
Raphael.left(90)
Raphael.forward(235)
Raphael.end_fill()


turtle.exitonclick()
