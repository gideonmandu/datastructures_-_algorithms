from rich import print


def bubble_sort(my_list: list) -> list:
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


if __name__ == "__main__":
    test_list = [1, 5, 3, 6, 9, 3, 5, 0]
    print(bubble_sort(test_list))
