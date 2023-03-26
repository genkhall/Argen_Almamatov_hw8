def bubble_sort(lst):
    n = len(lst)
    count_num = 0
    for run in range(n - 1):
        for i in range(n - 1 - run):
            count_num += 1
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print(f'количество обходов: {count_num}')
    return lst


# bubble_sort()


one_list = [1, 8, 3, 4, 2, 9, 7, 6, 5, 10]
sorted_list = bubble_sort(one_list)
print(sorted_list)


def selection_sort(lst_1):
    n = len(lst_1)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst_1[j] < lst_1[min_idx]:
                min_idx = j
        lst_1[i], lst_1[min_idx] = lst_1[min_idx], lst_1[i]

    return lst_1


my_list = [9, 5, 1, 2, 4, 7, 3]
sorted_list2 = selection_sort(my_list)
print(sorted_list2)


