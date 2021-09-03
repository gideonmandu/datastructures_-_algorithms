from rich import print


def print_numbers(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


def add_item(n):
    return n + n


l = [1, 2, 3, 4, 5, 6, 7, 8]


if __name__ == "__main__":
    add_item(10)
