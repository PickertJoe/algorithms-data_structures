# A class to simulate the behavior of a linked list that keeps all nodes in numerical order

from node_class import Node


class OrderedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def isEmpty(self):
        return self.len == 0

    def length(self):
        return self.len

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        self.len += 1

    def remove(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            print("Sorry, but the number you requested is not in the list.")
            return False
        else:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            self.len -= 1
