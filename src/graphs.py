from rich import print


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def __str__(self):
        graph = ""
        for vertex in self.adj_list:
            graph += f"{vertex} : {self.adj_list[vertex]}, "
        return graph


my_graph = Graph()
my_graph.add_vertex("A")
print(my_graph)
