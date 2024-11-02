class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            return "ERROR: The stack is empty!"

    def peek(self):
        try:
            return self.__items[len(self.__items) - 1]
        except IndexError:
            return "ERROR: The stack is empty!"