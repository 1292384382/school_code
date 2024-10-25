def join_multiply(first_list, second_list, result_list,first_list_flag=True,second_list_flag=False):
    if len(first_list)==0 or len(second_list)==0:
        return []
    elif first_list_flag:
        result_list += join_multiply([first_list[0]],second_list, result_list, False, True)
        join_multiply(first_list[1:], second_list, result_list, True, False)
    elif second_list_flag:
        return [first_list[0] * second_list[0]] + join_multiply(first_list, second_list[1:], result_list, False, True)
#控制字符有点多，不知道能不能改