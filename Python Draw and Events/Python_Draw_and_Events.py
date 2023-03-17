import string
from turtle import Turtle, Screen, width
import random
#from ColorSearch import convert_rgb_to_names, randomColor

#Function to move forward the turtle object received 
def moveForward(tTurtle, iDistance=10):
    tTurtle.forward(iDistance)

def moveBackward(iDistance=10):
    theTurtle.backward(iDistance)

def moveClockwise(iDistance=10):
    newHeading = theTurtle.heading() - iDistance
    theTurtle.setheading(newHeading)

def moveCounterClockwise(iDistance=10):
    newHeading = theTurtle.heading() + iDistance
    theTurtle.setheading(newHeading)

def cleanScreen():
    #theScreen.clearscreen()
    theTurtle.penup()
    theTurtle.clear()
    theTurtle.home()
    theTurtle.pendown()

#Open Tturtle Screen Window
isRaceOn = False
theScreen = Screen()
dColors = ["red", "orange", "yellow", "green", "blue", "purple"]

#General Parameters
iStep = 10  #distance turtle move on each turn
iWidth = 500
iHeight = 400
iMaxTurtles = 6

#Setup windows size 
theScreen.colormode(255)

theScreen.setup(width=iWidth ,height=iHeight)  #Use keyboard argument (name) to be more easy to maintain

#ask for the how many turtles on the race 
iTurtleNumber = theScreen.numinput(title="Turtle Race", prompt="How many turtles on the race?", maxval=iMaxTurtles )

sPrompt = "Which Turtle will win the race: "
for i in range(int(iTurtleNumber)):
        sPrompt = sPrompt + " - " + string.capwords(dColors[i])
sPrompt = sPrompt + "?" 
#ask for the turtle winner (by Color)
userBet = theScreen.textinput(title="Choose the Winner!", prompt=sPrompt)

#Create Turtles object and asign a shape
theTurtles = []
iDistance = iHeight/iTurtleNumber
startY = ((iHeight/2)*-1)+(iDistance/2)
for i in range(int(iTurtleNumber)):
    theTurtles.append(i)
    theTurtles[i]= Turtle(shape="turtle")
    tempTurtle = theTurtles[i]
    tempTurtle.color(dColors[i])
    tempTurtle.penup()
    tempTurtle.goto(x=-250, y=(startY+(iDistance*i)))

if userBet:
    isRaceOn = True

#calculate finist line position (X coordinate). .Turtle if 40x40
iFinishLine = iWidth / 2 - 20

while isRaceOn:
    for iTurtle in theTurtles:
        iDistance = random.randint(0, iStep)    
        moveForward(iTurtle, iDistance)
        if iTurtle.xcor()> iFinishLine:
            sWinningColor = iTurtle.pencolor()
            if sWinningColor.lower() == userBet.lower():
                print (f"You've won!! The {sWinningColor} turtle is the winner!")
            else:
                print (f"You lost!! The {sWinningColor} turtle is the winner!")
            isRaceOn = False

#other exercise
#MANUAL MOVEMENTS
#Keys W(Forward)  S(Backwards) A(Counter Clockwise) D (Clockwise)  C(Clear Screen and Turtle on center of screen)
#Lower Caps Options
#theTurtle = Turtle(shape="turtle")
#theTurtle.color("black")
#theTurtle.penup()
#theTurtle.goto(x=-250, y=((iHeight/2)-(iDistance/2/2)))
#theScreen.listen()
#theScreen.onkey(key="w",fun=moveForward)   #This is a sample of a higher order function
#theScreen.onkey(key="s",fun=moveBackward)   #This is a sample of a higher order function
#theScreen.onkey(key="a",fun=moveCounterClockwise)   #This is a sample of a higher order function
#theScreen.onkey(key="d",fun=moveClockwise)   #This is a sample of a higher order function
#theScreen.onkey(key="c",fun=cleanScreen)   #This is a sample of a higher order function
###Upper Caps Options
#theScreen.onkey(key="W",fun=moveForward)   #This is a sample of a higher order function
#theScreen.onkey(key="S",fun=moveBackward)   #This is a sample of a higher order function
#theScreen.onkey(key="A",fun=moveCounterClockwise)   #This is a sample of a higher order function
#theScreen.onkey(key="D",fun=moveClockwise)   #This is a sample of a higher order function
#theScreen.onkey(key="C",fun=cleanScreen)   #This is a sample of a higher order function


theScreen.exitonclick()