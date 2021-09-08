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
    for j in list2:
        return list_dict[j]
