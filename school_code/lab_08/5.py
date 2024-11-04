def mirror_queue(a_queue):
    st=Stack()
    for i in range(a_queue.size()):
        temp=a_queue.dequeue()
        st.push(temp)
        a_queue.enqueue(temp)
    for i in range(st.size()):
        a_queue.enqueue(st.pop())