def bubble_sort(my_list):
    i = len(my_list)-1
    while (i!= 0):
        for j in range(i):
            if my_list[j]>my_list[j+1]:
                temp = my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
        i-=1


    # for i in range(len(my_list) - 1, 0 ,-1):
    #     for j in range(i):
    #         if my_list[j] > my_list[j+1]:
    #             temp = my_list[j]
    #             my_list[j] = my_list[j+1]
    #             my_list[j+1] = temp
    return my_list

my_list = [3, 7, 1, 9, 2, 6, 8, 4, 5, 10]

my_list = bubble_sort(my_list)
print(my_list)