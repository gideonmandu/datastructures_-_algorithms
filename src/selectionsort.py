from rich import print


def selection_sort(my_list: list) -> list:
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


if __name__ == "__main__":
    test_list = [1, 5, 3, 6, 9, 3, 5, 0]
    print(selection_sort(test_list))
