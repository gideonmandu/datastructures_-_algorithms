from rich import print


def swap(array: list, index, swap):
    temp = array[index]
    array[index] = array[swap]
    array[swap] = temp


def pivot(list_to_sort: list, pivot_index: int, end_index: int) -> int:
    """Rearranges values in list with less than items on the left
    and greater than items on the right of the pivot index

    Args:
        list_to_sort (list): list to sort
        pivot_index (int): point to compare from
        end_index (int): index of last item on list

    Returns:
        int: index of value user for comparison
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if list_to_sort[i] < list_to_sort[pivot_index]:
            swap_index += 1
            swap(list_to_sort, swap_index, i)
    swap(list_to_sort, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(list_to_sort: list, left: int, right: int):
    """Sorts list from smallest to largest

    Args:
        list_to_sort (list): list to sort
        left (int): left most index in list
        right (int): right most index in list
    """
    if left < right:
        pivot_index = pivot(
            list_to_sort=list_to_sort, pivot_index=left, end_index=right
        )
        quick_sort_helper(
            list_to_sort=list_to_sort, left=left, right=pivot_index-1
        )
        quick_sort_helper(
            list_to_sort=list_to_sort, left=pivot_index+1, right=right
        )
    return list_to_sort


def quick_sort(list_to_sort):
    return quick_sort_helper(
        list_to_sort=list_to_sort, left=0, right=len(list_to_sort)-1
    )


if __name__ == "__main__":
    my_list = [4, 6, 1, 7, 3, 2, 5]
    print(quick_sort(my_list))
