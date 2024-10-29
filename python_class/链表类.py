class listnode:
    def __init__(self,x):
        self.val=x
        self.next=None
    def add_next(self,x):
        self.next=x
    def value_listnode(self):
        return self.val
    def return_next(self):
        return self.next
node3 = listnode(3)
node5 = listnode(5)
node6 = listnode(6)
node1 = listnode(1)
node3.add_next(node5)
node5.add_next(node6)
node6.add_next(node1)
current=node3
while current:
    print(current.value_listnode())
    current=current.return_next()