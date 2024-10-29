import test
def shift(arr,current,index,current_index):#如果我需要替换多个数，我需要写出shift函数来批量替换
    new_list=arr[:index]+[current]+arr[index:current_index]+arr[current_index+1:]#右移数组
    arr[:]=new_list#深拷贝
def find_index(arr,i,current):#i表示排序区到哪了
    left_pointer=0
    right_pointer=i-1
    flag=False#标志有没有进入判断，如果没有返回原本的index，如果有返回right_pointer
    while left_pointer < right_pointer:#进行多次比较之后，如果右指针比左指针小，说明这个时候右指针的右边就是值要插入的地方
        flag=True
        mid_pointer=int((left_pointer+right_pointer)/2)#取中间指针，向下取整
        if current >= arr[mid_pointer]:
            left_pointer=mid_pointer+1#通过比较中间指针缩小范围
        else:
            right_pointer=mid_pointer-1#通过比较中间指针缩小范围
            if right_pointer < 0:
                right_pointer=0
                break
    if flag:
        return right_pointer
    else:
        return i

def half_insert_sorted(arr):
    for i in range(len(arr)):#最低期望是n次结束
        current=arr[i]
        if not current > arr[i-1]:
            index=find_index(arr,i,current)#查找要插入值的地方
            shift(arr,current,index,i)#移动值并插入
    return arr
'''
while j >= high + 1:
            mylist[j + 1] = mylist[j]
            j -= 1
            后移也用这个
'''
half_insert_sorted(test.list1)
