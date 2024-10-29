# https://www.runoob.com/w3cnote/shell-sort.html
"""
选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
按增量序列个数 k，对序列进行 k 趟排序；
每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
"""
import test


def xier_sorted(arr):
    d = int(len(arr) / 2)#一般步长最开始是数列的一半，有时也从3分之一开始取数
    while d > 0:
        for i in range(d):#总结规律我们可以发现如果我们需要循环的次数就是步长次
            for k in range(int(len(arr) / d)):#我们根据步长
                preindex = i + (k - 1) * d
                current = arr[i + k * d]
                while preindex >= 0 and arr[preindex] > current:
                    arr[preindex + d] = arr[preindex]
                    preindex -= d
                arr[preindex + d] = current
        d = int(d / 2)
    return arr


xier_sorted(test.list1)
