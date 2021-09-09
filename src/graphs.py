from rich import print


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if (v1 and v2) in self.adj_list.keys(): 
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def __str__(self):
        graph = {}
        for vertex in self.adj_list:
            graph[vertex] = self.adj_list[vertex]
        return str(graph)


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
print(my_graph)
my_graph.add_edge(1, 2)
print(my_graph)
