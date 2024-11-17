class EvenNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return EvenIterator(self.numbers)
class EvenIterator:
    def __init__(self,list):
        self.list=list
        self.point=0
    def __next__(self):
        while self.point<len(self.list):
            if self.list[self.point]%2==0:
                a=self.list[self.point]
                self.point+=1
                return a
            else:
                self.point+=1
        raise StopIteration
nums = EvenNumbers([1, 2, 3, 4, 5, 6, 7, 8])
for even_num in nums:
    print(even_num)