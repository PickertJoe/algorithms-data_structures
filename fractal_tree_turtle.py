# A program to draw a simple fractal tree using the turtle module

from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)
