class CircularQueue:
    def __init__(self,count=8):
        self.__count=0
        self.__front=0
        self.__back=count-1
        self.__items=[None for i in range(count)]
        self.lens=len( self.__items)
    def is_empty(self):
        if self.__count==0:
            return True
        return False
    def __str__(self):
        return f"{self.__items}, front:{self.__front}, back:{self.__back}, count:{self.__count}"
    def is_full(self):
        if self.__count==self.lens:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.is_full():
            print("ERROR: The queue is full.")
            raise IndexError
        else:
            self.__back = (1 + self.__back) % self.lens
            self.__items[self.__back]=item
            self.__count+=1
    def dequeue(self):
        if self.is_empty():
            print("ERROR: The queue is empty.")
            raise IndexError
        else:
            a=self.__items[self.__front]
            self.__front=(1+self.__front)%self.lens
            self.__count-=1
            return a
