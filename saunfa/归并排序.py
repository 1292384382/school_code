def guibin_sort(arr,begin=None,end=None):
    if begin==None:
        begin=0
    if end==None:
        end=len(arr)-1
    mid_point=int((begin+end)/2)
    first_list=arr[:mid_point]
    second_list=arr[mid_point:]


