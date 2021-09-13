from rich import print


def insertion_sort(my_list: list) -> list:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


test_list = [1, 5, 3, 6, 9, 3, 5, 0]
print(insertion_sort(test_list))
