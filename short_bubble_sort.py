# A more efficient bubble sort algorithm. Sourced from Miller & Ranum
# This algorithm will recognize if a list is already sorted and stop early


def shortBubbleSort(alist):
    exchanges = True
    passnumber = len(alist) - 1
    while passnumber > 0 and exchanges:
        exchanges = False
        for i in range(passnumber):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnumber += 1
