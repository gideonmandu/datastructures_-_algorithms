from rich import print
from merge import merge


def merge_sort(list_to_sort: list) -> list:
    # base case
    if len(list_to_sort) == 1:
        return list_to_sort
    # break list in halves
    mid = int(len(list_to_sort) / 2)
    left = list_to_sort[:mid]
    right = list_to_sort[mid:]
    # merge list
    return merge(merge_sort(left), merge_sort(right))

if __name__ == "__main__":
    test = [1, 9, 5, 3, 4, 2, 8, 0]
    print(merge_sort(test))
