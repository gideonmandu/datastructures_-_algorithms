from rich import print


class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size

    def __hash(self, key: str):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        """Adds a key value pair to the hashtable

        Args:
            key ([type]): [description]
            value ([type]): [description]
        """
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        return [
            self.data_map[i][j][0]
            for i in range(len(self.data_map))
            if self.data_map[i] is not None
            for j in range(len(self.data_map[i]))
        ]

    def __str__(self):
        display = "{"
        for i, v in enumerate(self.data_map):
            display += f"{i}: {v}, "
        return display.strip(", ") + "}"


if __name__ == "__main__":
    my_hash = HashTable()
    print(my_hash)
    my_hash.set_item("bolts", 12)
    my_hash.set_item("washers", 50)
    my_hash.set_item("screws", 10)
    print(my_hash)
    print(my_hash.get_item("screws"))
    print(my_hash.keys())
