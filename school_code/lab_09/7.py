class LinkedList:
    def __init__(self):
        self.__head=None
        self.count=0
        self.point=None
    def add(self, value):
        if self.__head is not None:
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
        if self.__head is None:
            return True
        else:
            return False
    def __len__(self):
        return self.count
    def __str__(self):
        result_list=[]
        a=self.__head
        while a is not None:
            result_list+=[str(a.get_data())]
            a=a.get_next()
        temp_string=", ".join(result_list)
        result_string="["+temp_string+"]"
        return result_string
    def __contains__(self, search_value):
        a=self.__head
        while a is not None:
            if a.get_data() == search_value:
                return True
            a=a.get_next()
        return False

    def __getitem__(self, index):
        a=self.__head
        for i in range(index):
            a=a.get_next()
        return a.get_data()
    def add_all(self, a_list):
        for i in a_list:
            self.add(i)
            
