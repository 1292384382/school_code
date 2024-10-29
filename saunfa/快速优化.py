import random
import test
def kuaisu_sort(arr, begin=None, end=None):
        if begin is None:
            begin = 0
        if end is None:
            end = len(arr)

        if end - begin > 1:
            pivot = arr[begin]
            left_point = begin
            right_point = end - 1

            while left_point < right_point:
                while arr[right_point] >= pivot and right_point > left_point:
                    right_point -= 1
                arr[left_point] = arr[right_point]

                while arr[left_point] <= pivot and left_point < right_point:
                    left_point += 1
                arr[right_point] = arr[left_point]

            arr[right_point] = pivot
            kuaisu_sort(arr, begin, right_point)
            kuaisu_sort(arr, right_point + 1, end)

kuaisu_sort(test.list1)


