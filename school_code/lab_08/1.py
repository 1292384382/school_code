class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        try:
            return self.__items.pop()
        except IndexError:
            return "ERROR: The queue is empty!"

    def size(self):
        return len(self.__items)

    def peek(self):
        try:
            return self.__items[len(self.__items)-1]
        except IndexError:
            return "ERROR: The queue is empty!"