# A program that uses recursion to solve a simple maze
# Base code sourced from Miller and Ranum's Problem Solving with Algorithms & Data Structures Using Python

from Turtle import *


class Maze:
    def __init__(self, mazeFileName):
        rowsinMaze = 0
        columnsinMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        rowsinMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsinMaze
                    self.startCol = col
                col += 1
            rowsinMaze += 1
            self.mazelist.append(rowList)
            columnsinMaze = len(rowList)

        self.rowsinMaze = rowsinMaze
        self.columnsinMaze = columnsinMaze
        self.xTranslate = -columnsinMaze / 2
        self.yTranslate = rowsinMaze / 2
        self.t = Turtle(shape='turle')
        setup(width=600, height=600)
        setworldcoordinates(-(columnsinMaze - 1) / 2 - .5,
                            -(rowsinMaze - 1) / 2 - .5,
                            (columnsinMaze - 1) / 2 + .5,
                            (rowsinMaze - 1) / 2 + .5)

    def drawMaze(self):
        for y in range(self.rowsinMaze):
            for x in range(self.columnsinMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x + self.xTranslate,
                                         -y + self.yTranslate,
                                         'tan')
        self.t.color('black', 'blue')

    def drawCenteredBox(self, x, y, color):
        tracer(0)
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.being_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()
        tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate,
                                         -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or
                row == self.rowsinMaze - 1 or
                col == 0 or
                col == self.columnsinMaze - 1)

    def __getitem__(self, idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startCol):
    maze.updatePosition(startRow, startCol)
    # Checking for base case
    # 1) If an obstacle is encountered, return false
    if maze[startRow][startCol] == OBSTACLE:
        return False

    # 2) If a square is encountered that has already been explored, return false
    if maze[startRow][startCol] == TRIED:
        return False

    # 3) If an outside edge is open and encountered, return true
    if maze.isExit(startRow, startCol):
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startCol, TRIED)

    found = searchFrom(maze, startRow - 1, startCol) or \
        searchFrom(maze, startRow + 1, startCol) or \
        searchFrom(maze, startRow, startCol - 1) or \
        searchFrom(maze, startRow, startCol + 1)

    if found:
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startCol, DEAD_END)
    return found
