# A program to draw a spiral using turtle graphics
# This code cannot be properly run in Sublime Text and should be copy/pasted into
# The default Python IDLE editor

from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()


def drawSpiral(myTurtle, lineLen):
    if len > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)


drawSpiral(myTurtle, 100)
myWin.exitonclick()
