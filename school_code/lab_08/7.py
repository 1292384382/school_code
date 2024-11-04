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

