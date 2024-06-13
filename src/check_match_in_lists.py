from rich import print


def item_in_common(list1: list, list2: list) -> bool:
    """Checks if two items in match O(n^2)

    Args:
        list1 (list): first list
        list2 (list): second list

    Returns:
        bool: if true found match else no match
    """
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


def item_in_common2(list1: list, list2: list) -> bool:
    """Checks if two items in match O(n)

    Args:
        list1 (list): first list
        list2 (list): second list

    Returns:
        bool: if true found match else no match
    """
    list_dict = {i: True for i in list1}
    return any(j in list_dict for j in list2)


if __name__ == "__main__":
    l1 = [1,2,3,4,5]
    l2 = [9,8,7,6,5]
    print(f"O(n^2) {item_in_common(l1,l2)}")
    print(f"{item_in_common2(l1,l2)}")