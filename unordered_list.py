# A class to simulate the ADT of unordered lists
# The methods isEmpty, add, length, search, and remove were included by Miller & Ranum in the text
# The methods append, insert, index, and pop were implimented by me


from node_class import Node


class UnorderedList:
    """Simulates an unordered list using a linked list"""

    def __init__(self):
        self.head = None
        self.len = 0

    def isEmpty(self):
        return self.len == 0

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.len += 1

    def length(self):
        return self.len

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == item:
                found = True
            elif current is None:
                print("Sorry, but the number you requested is not in the list.")
                return False
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.len -= 1

    def pop(self, index=0):
        current = self.head
        previous = None
        current_position = 0

        if index == 0:
            position = self.length()
        else:
            position = self.length() - (index + 1)

        while current.getNext() and (current_position < position):
            previous = current
            current = current.getNext()
            current_position += 1

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.len -= 1

        return current.getData()

    def append(self, item):
        current = self.head
        while current.getNext():
            current = current.getNext()

        temp = Node(item)
        current.setNext(temp)

        self.len += 1

    def index(self, item):
        current = self.head
        found = False
        counter = self.length() - 1
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                counter -= 1

        if found is False:
            print("Sorry, but that number was not found in this list")

        else:
            return counter

    def insert(self, item, index):
        current = self.head
        previous = None
        counter = self.length() - 1
        while counter > index:
            previous = current
            current = current.getNext()
            counter -= 1

        temp = Node(item)
        if previous is None:
            self.head = temp

        previous.setNext(temp)
        temp.setNext(current)

        self.len += 1
