# A program that employs recursion to generate a Koch snowflake using turtle graphics
# This document is just to hold the code to create a fractal tree
# To run this program, copy and past each line into the default IDLE shell

from turtle import *

t = Turtle()
myWin = t.getscreen()


def koch(turtle, order, size):

    if order == 0:
        t.forward(size)

    else:
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)
        t.right(120)
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)


t.down()
koch(t, 3, 500)
