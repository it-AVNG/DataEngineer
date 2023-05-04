def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

    

my_list = [3, 7, 1, 9, 2, 6, 8, 4, 5, 10]

my_list = selection_sort(my_list)
print(my_list)