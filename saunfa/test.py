def shift(arr, current, index):
    arr.remove(current)  # 移除当前元素
    arr.insert(index, current)  # 在指定位置插入
    return arr

def find_index(arr, i, current):
    left_pointer = 0
    right_pointer = i - 1
    while left_pointer <= right_pointer:  # 使用 <=
        mid_pointer = (left_pointer + right_pointer) // 2
        if current >= arr[mid_pointer]:
            left_pointer = mid_pointer + 1
        else:
            right_pointer = mid_pointer - 1
    return left_pointer  # 返回插入位置

def half_insert_sorted(arr):
    for i in range(len(arr)):
        current = arr[i]
        if i == 0 or current < arr[i - 1]:  # 只在需要插入时进行操作
            index = find_index(arr, i, current)
            shift(arr, current, index)
    return arr

print(half_insert_sorted([3, 2, 4, 5, 63, 5, 7, 6565, 767, 34242, 66878, 222, 1, 1]))