def mirror_queue(a_queue):
    st=Stack()
    for i in range(a_queue.size()):
        temp=a_queue.dequeue()
        st.push(temp)
        a_queue.enqueue(temp)
    for i in range(st.size()):
        if a_queue.dequeue() != st.pop():
            return False
    return True
def is_palindrome(word):
    a_queue=Queue()
    for i in word:
        a_queue.enqueue(i)
    return mirror_queue(a_queue)
