class LinkedList:
    def __init__(self):
        self.__head=None
        self.count=0
        self.point=None
    def add(self, value):
        if self.__head != None:
            temp=Node(value,self.__head)
            self.__head=temp
            self.count+=1
        else:
            self.__head=Node(value)
            self.point=self.__head
            self.count+=1
    def size(self):
        return self.count
    def get_head(self):
        return self.__head
    def clear(self):
        self.__head=None
        self.count=0
    def is_empty(self):
        if self.__head==None:
            return True
        else:
            return False
    def __len__(self):
        return self.count