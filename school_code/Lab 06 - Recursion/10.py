def binary_search(values, item):
    right_point=0
    left_point=len(values)
    mid_point=int((right_point+left_point)/2)
    if values[mid_point] != item:
        print(f"{values[right_point:mid_point]} {values[mid_point]} {values[mid_point + 1:left_point]}")
        if right_point==mid_point:
            return False
        elif values[mid_point] > item:
            result=binary_search(values[right_point:mid_point], item)
        elif values[mid_point] <= item:
            result=binary_search(values[mid_point+1:left_point],item)
        return result
    else:
        print(f"{values[right_point:mid_point]} {values[mid_point]} {values[mid_point+1:left_point]}")
        return True
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))