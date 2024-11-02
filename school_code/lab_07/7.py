
def reverse_sentence(sentence):
    temp=Stack()
    sentence=list(sentence.split())
    for i in sentence:
        temp.push(i)
    temp1=""
    for i in range(temp.size()):
        temp1+=temp.peek()+" "
        temp.pop()
    return temp1

