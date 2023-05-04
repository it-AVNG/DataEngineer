def merge(list1,list2):
    combine_list = []
    i=0; j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combine_list.append(list1[i])
            i += 1
        else:
            combine_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        combine_list.append(list1[i])
        i += 1

    while j < len(list2):
        combine_list.append(list2[j])
        j += 1    
    
    return combine_list



def merge_sort(my_list):
    if len(my_list) == 1:
      return my_list
    mid_index = int(len(my_list)/2)

    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

my_list = [3,5,4,7,1,8,9,0,2]
print(merge_sort(my_list))