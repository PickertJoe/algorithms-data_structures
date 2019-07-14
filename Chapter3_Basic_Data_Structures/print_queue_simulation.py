# A program to simulate average waiting time for a computer lab printer- Miller and Ranum

from pythonds.basic import Queue
import random
from printer_class import Printer
from task_class import Task


def main():
    """Function to serve as main menu and driver"""


def simulation(numSeconds, pagesPerMinute):
    """Performs the modeling of average printer wait time"""

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if ((not labprinter.busy()) and (not printQueue.isEmpty())):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f seconds %3d tasks remaining." % (averageWait.printQueue.size()))


def newPrintTask():
    """Randomly generates a printing task assuming 20/hour"""
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False
