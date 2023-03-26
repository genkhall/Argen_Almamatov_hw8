def binary_search(x, lst):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if x == lst[mid]:
            return mid
        elif x > lst[mid]:
            first = mid + 1
        else:
            last -= 1
    return None


lst = [1, 3, 4, 6, 8, 9, 11]
x = 6
result = binary_search(x, lst)

if result is not None:
    print(f"Элемент {x} найден в списке на позиции {result}")
else:
    print(f"Элемент {x} не найден в списке")
