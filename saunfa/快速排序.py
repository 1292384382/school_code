import random
import test
def quick_sort(arr):
    if len(arr)!=0:
        right_point=0
        left_point=len(arr)-1
        current=arr[0]
        new_list_right=[]
        new_list_left=[]
        for i in range(1,len(arr)):
            if current > arr[i]:
                new_list_right+=[arr[i]]
                right_point+=1
            elif current < arr[i]:
                new_list_left+=[arr[i]]
                left_point-=1
        return quick_sort(new_list_right)+[current]+quick_sort(new_list_left)
    else:
        return []

quick_sort(test.list1)