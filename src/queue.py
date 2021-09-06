from rich import print


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is not None:
            self.last.next = new_node
        else:
            self.first = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def __str__(self):
        queue = "["
        temp = self.first
        while temp is not None:
            queue += f"{temp.value}, "
            temp = temp.next
        return f"{queue.strip(', ')}]"


my_queue = Queue(0)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue)
my_queue.dequeue()
print(my_queue)
