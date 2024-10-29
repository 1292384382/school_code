import test


def chuli_arr(arr):
    new_list = [0]
    new_list += arr
    arr[:] = new_list
    return arr
def fanhui_arr(arr):
    arr = arr[1:]
    return arr
def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]
def swap_heap(arr,index):
    left_child=index*2
    right_child=index*2+1
    largest=index
    if right_child<=arr_len-1 and arr[right_child]>arr[largest]:
        largest=right_child
    if left_child<=arr_len-1 and arr[left_child]>arr[largest]:
        largest=left_child
    if index != largest:
        swap(arr,index,largest)
        swap_heap(arr,largest)
def build_heap(arr):
    arr=chuli_arr(arr)
    index=int((len(arr)-1)/2)
    for i in range(index,0,-1):
        swap_heap(arr,i)
def heap_sort(arr):
    global arr_len#惊为天人的一笔，通过global arr_len变量，不仅简单声明了列表的长度避免重复使用，而且通过在循环里面通过children<arr_len-1来逐步排除最后一个数，从而达到堆排序在把最大值移到最后之后排除最大值，天才！
    arr_len=len(arr)
    build_heap(arr)
    for i in range(1,len(arr)-1):
        swap(arr,1,len(arr)-i)
        swap_heap(arr,1)
        arr_len-=1
    arr[:]=arr[1:]
heap_sort(test.list1)