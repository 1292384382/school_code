#https://www.runoob.com/w3cnote/insertion-sort.html
import time
import random
def insert_sorted(arr):
    for i in range(len(arr)):#最低期望是n次结束
        preindex=i-1
        current=arr[i]
        while preindex>=0 and arr[preindex] > current:#这个判断是排除i=0时没有前一位和把之前排序完成的数比current大的都前移
            arr[preindex+1]=arr[preindex]#迁移数组，下一次循环后面一位会自动替换，或者结束循环后current会自动不上
            preindex-=1#前一位继续进行比较，如果下一位不比current大，循环结束，但是index依然会减一，所以最后preindex要加一
        arr[preindex+1]=current#插入current
    return arr
list1=[]
for i in range(100000000):
    list1+=[i]
random.shuffle(list1)
print(insert_sorted(list1))
