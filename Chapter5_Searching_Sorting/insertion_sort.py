# A simple function to perform an insertion sort to order a numeric list. Sourced from Miller & Ranum


def insertionSort(alist):
    for i in range(1, len(alist)):

        currentvalue = alist[i]
        position = i

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue
