class stack:
    def __init__(self):
        self.context=[]
        self.point=None
    def add(self,x):
        self.context+=[x]
        if self.point is None:
            self.point=0
        else:
            self.point+=1
    def return_stack(self):
        temp=self.context[self.point]
        self.context.remove(temp)
        self.point-=1
        return temp
    def show_stack(self):
        return self.context
stack1=stack()
stack1.add(1)
stack1.add(2)
print(stack1.return_stack())
print(stack1.show_stack())
