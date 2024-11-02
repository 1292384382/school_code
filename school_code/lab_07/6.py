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

    def __str__(self):
        return f"Stack: {self.__items}"

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def push_list(self, a_list):
        for i in a_list:
            self.push(i)

    def multi_pop(self, number):
        if number <= self.__len__():
            for i in range(number):
                x = self.pop()
            return True
        else:
            return False
    def copy(self):
        a=Stack()
        a.push_list(self.__items[:])
        return a
    def show(self):
        return self.__items
    def __eq__(self, other):
        if str(type(other))=="<class '__main__.Stack'>":
            if other.show()==self.__items:
                return True
        return False