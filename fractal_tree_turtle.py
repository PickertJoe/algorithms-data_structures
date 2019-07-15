# A program to draw a simple fractal tree using the turtle module
# This document is just to hold the code to create a fractal tree
# To run this program, copy and past each line into the default IDLE shell

from turtle import *

t = Turtle()
myWin = t.getscreen()


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)


t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')


tree(110, t)
