#https://www.runoob.com/w3cnote/selection-sort.html
'''
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕
'''
def selectionSort(arr):
    for i in range(len(arr)):#最小期望是n
        min_index=i
        for k in range(len(arr)):
            if arr[k]<arr[min_index]:
                min_index=k#找到数组中最小数的那个索引
        arr[i],arr[min_index]=arr[min_index],arr[i]#外层的i不止作为计数器，也作为最小数位置标志，将最小数放进最小数位置里
    return arr
print(selectionSort([3,2,4,5,63,5,7,6565,767,34242,66878,222,1,1]))
