def get_consecutive_sum(first_node):
    a=first_node
    result_list=[]
    while a != None:
        result_list+=[a.get_sum()]
        a=a.get_next()
    return result_list