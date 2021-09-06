from rich import print


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height != 0:
            new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def __str__(self):
        stack = "["
        temp = self.top
        while temp is not None:
            stack += f"{temp.value}, "
            temp = temp.next
        return stack.strip(", ") + "]"


my_stack = Stack(4)
my_stack.push(5)
my_stack.push(7)
print(my_stack)
my_stack.pop()
print(my_stack)
