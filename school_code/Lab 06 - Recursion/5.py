def get_merge_list(list_of_lists):
    if len(list_of_lists)==0:
        return []
    else:
        return list_of_lists[0]+get_merge_list(list_of_lists[1:])