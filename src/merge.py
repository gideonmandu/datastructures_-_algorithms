from rich import print


def merge(sorted_list1: list, sorted_list2: list) -> list:
    combined = []
    i = 0
    j = 0
    while i < len(sorted_list1) and j < len(sorted_list2):
        if sorted_list1[i] < sorted_list2[j]:
            combined.append(sorted_list1[i])
            i += 1
        else:
            combined.append(sorted_list2[j])
            j += 1
    while i < len(sorted_list1):
        combined.append(sorted_list1[i])
        i += 1
    while j < len(sorted_list2):
        combined.append(sorted_list2[j])
        j += 1
    return combined


if __name__ == "__main__":
    print(merge([1, 2, 3, 6], [9, 4, 7, 8]))
