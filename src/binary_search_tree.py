from rich import print


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self) -> list:
        """Breath first Search

        Returns:
            list: list of values from tree
        """
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while queue:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def DFS_pre_order(self) -> list:
        """Depth first search of tree using a pre order technique

        Returns:
            list: list of values from list
        """
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

    def DFS_post_order(self) -> list:
        """Depth first search using a post order technique

        Returns:
            list: list of values from list
        """
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def DFS_in_order(self) -> list:
        """Depth first search using in order technique

        Returns:
            list: list of values from list
        """
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            else:
                result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
            # else:
            #     result.append(current_node.value)
        traverse(self.root)
        return result


my_tree = BinarySearchTree()
print(my_tree.root)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(30)
my_tree.insert(15)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(1))
print(my_tree.BFS())
print(my_tree.DFS_pre_order())
print(my_tree.DFS_post_order())
print(my_tree.DFS_in_order())
