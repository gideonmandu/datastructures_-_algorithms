from rich import print


class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size

    def __hash(self, key: str):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def __str__(self):
        display = "{"
        for i, v in enumerate(self.data_map):
            display += f"{i}: {v}, "
        return display.strip(", ") + "}"


my_hash = HashTable()
print(my_hash)
