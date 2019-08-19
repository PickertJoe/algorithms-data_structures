# A simple function to perform a bubble sort algorithm to order a numeric list. Sourced from Miller & Ranum


def bubbleSort(alist):
    for iteration in range(len(alist) - 1, 0, -1):
        for i in range(iteration):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
