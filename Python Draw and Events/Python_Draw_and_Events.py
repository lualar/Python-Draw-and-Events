import random
from turtle import Turtle, Screen
from ColorSearch import convert_rgb_to_names, randomColor

#Create Turtle object and asign a shape
theTurtle = Turtle()
theTurtle.shape("turtle")
theTurtle.color("green")


#Open Tturtle Screen Window
theScreen = Screen()
theScreen.colormode(255)
theScreen.exitonclick()
