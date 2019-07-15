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
