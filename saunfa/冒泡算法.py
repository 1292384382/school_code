# https://www.runoob.com/w3cnote/bubble-sort.html
"""
比较相邻的元素。如果第一个比第二个大，就交换他们两个。

对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

针对所有的元素重复以上的步骤，除了最后一个。

持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
import test


def bubble_sort(arr):
    for i in range(len(arr)):  # 外层循环执行n次，程序的最低执行期望就是n次
        for j in range(1, len(arr)):  #
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


bubble_sort(test.list1)
