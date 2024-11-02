def balanced_brackets(text):
    a=Stack()
    dictoriny={")":"(",">":"<"}
    for i in text:
        if i=="(" or i=="<":
            a.push(i)
        elif i==")" or i==">":
            if a.is_empty():
                return False
            if a.peek()==dictoriny[i]:
                a.pop()
            else:
                return False
    return a.is_empty()