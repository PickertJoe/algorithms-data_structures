# A function to perfrom a binary search recursively without using slice operator


def binarySearch(alist, item):
    start = 0
    end = len(alist) - 1
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                end = midpoint - 1
                return binarySearch(alist[start, end], item)
            else:
                start = midpoint + 1
                return binarySearch(alist[start, end], item)


# Testing our sorting function
testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

binarySearch(testlist, 5)
