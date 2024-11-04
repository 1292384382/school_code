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
    def __str__(self):
        a=self.__items[:]
        a.reverse()
        return f"Queue: {a}"
    def __len__(self):
        return len(self.__items)
    def clear(self):
        self.__items = []
    def enqueue_list(self, a_list):
        for i in range(len(a_list)):
            self.enqueue(a_list[i])