import queue


class UnidirectedGraph(object):
    """Docstring for MyClass. """

    def __init__(self, vertices):
        """TODO: to be defined."""
        self.adjacency_matrix = []
        for item in range(vertices):
            self.adjacency_matrix.append([0] * vertices)

    def add_edge(self, source, destination):
        """docstring for add_edge"""
        """Adds an edge defined by vertices from source to destination
        then destination to source in matrix

        @param param:  source
        @param param:  destination
        """
        self.adjacency_matrix[source][destination] = 1
        self.adjacency_matrix[destination][source] = 1

    def get_vertex(self):
        """Generator for returning the next vertex from the adjacency list
        @return:
        """
        for v, _ in enumerate(self.adjacency_matrix):
            yield v

    def get_neighbor(self, vertex):
        """Generator for returning the next vertex adjacent to the given vertex
        @param param: vertex
        """
        for i, flag in enumerate(self.adjacency_matrix[vertex]):
            if flag == 1:
                yield i

    def dfs_util(self, vertex, parents):
        """docstring for dfs_util"""
        for u in self.get_neighbor(vertex):
            if u not in parents:
                print(vertex, u)
                parents[u] = vertex
                self.dfs_util(u, parents)

    def dfs_recursive(self):
        """docstring for dfs_recursive"""
        """Computes the parents for each vertex as determined through 
        depth-first-search
        ( though not too meaningful in an undirected weightless graph)

        @rtype :  dict
        """
        parents = {}
        self.dfs_util(0, parents)
        return parents

    def dfs_iterative(self):
        """docstring for dfs_iterative"""
        """Computes the parents for each vertex as determined through
        depth-first-search
        ( though not too meaningful in an undirected weightless graph )

        @return:  parents for each vertex
        @rtype :  dict
        """
        parents = {}
        to_visit = [0]

        while to_visit:
            v = to_visit.pop()

            for neighbor in self.get_neighbor(v):
                if neighbor not in parents:
                    print(neighbor, v)
                    parents[neighbor] = v
                    to_visit.append(neighbor)

        return parents

    def bfs(self):
        """docstring for bfs"""
        """ Computes the parents for each vertex as determined through breadth-first search

        @rtype : dict
        """
        parents = {}
        to_visit = queue.Queue()
        to_visit.put(0)

        while not to_visit.empty():
            v = to_visit.get()

            for neighbor in self.get_neighbor(v):
                if neighbor not in parents:
                    print(v, neighbor)
                    parents[neighbor] = v
                    to_visit.put(neighbor)

        return parents

    def is_bipartite(self):
        """docstring for is_bipartite"""
        """ Returns true if graph is bipartite

        @rtype :  bool
        """
        colorings = {}
        to_visit = queue.Queue()
        to_visit.put(0)
        colorings[0] = 0

        while not to_visit.empty():
            v = to_visit.get()

            for u in self.get_neighbor(v):

                if u not in colorings:
                    # color it with opposite color
                    colorings[u] = 1 - colorings[v] 
                    print(u, colorings)
                    to_visit.put(u)
                elif colorings[u] == colorings[v]:
                    return False

        return True


def get_test_graph_1():
    """docstring for get_test_graph_1"""
    udg = UnidirectedGraph(9)
    udg.add_edge(0, 1)
    udg.add_edge(1, 2)
    udg.add_edge(2, 3)
    udg.add_edge(1, 7)
    udg.add_edge(3, 7)
    udg.add_edge(7, 8)
    udg.add_edge(3, 4)
    udg.add_edge(3, 5)
    udg.add_edge(4, 5)
    udg.add_edge(5, 6)
    udg.add_edge(6, 7)
    udg.add_edge(6, 8)
    return udg


def get_test_graph_2():
    """docstring for get_test_graph_"""
    udg = UnidirectedGraph(8)
    udg.add_edge(0, 1)
    udg.add_edge(0, 5)
    udg.add_edge(2, 1)
    udg.add_edge(2, 3)
    udg.add_edge(2, 5)
    udg.add_edge(4, 3)
    udg.add_edge(4, 5)
    udg.add_edge(4, 7)
    udg.add_edge(6, 7)
    return udg


def test_dfs_recursive():
    """docstring for test_dfs_recursive"""
    udg = get_test_graph_1()
    p1 = udg.dfs_recursive()
    assert(p1 == {0: 1, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7})


def test_dfs_iterative():
    """docstring for test_bfs_iterative"""
    udg = get_test_graph_1()
    p1 = udg.dfs_iterative()
    assert(p1 == {0: 1, 1: 0, 2: 1, 3: 7, 4: 5, 5: 6, 6: 7, 7: 1, 8: 7})


def test_bfs():
    """docstring for test_bfs"""
    udg = get_test_graph_1()
    p1 = udg.bfs()
    assert(p1 == {0: 1, 1: 0, 2: 1, 3: 2, 4: 3, 5: 3, 6: 7, 7: 1, 8: 7})


def test_bitpartite():
    """docstring for test_bitpartite"""
    udg = get_test_graph_1()
    assert(udg.is_bipartite() == False)

    udg2 = get_test_graph_2()
    assert(udg2.is_bipartite() == True)


def main():
    """docstring for main"""
    # DFS
    test_dfs_recursive()
#     test_dfs_iterative()

    # BFS
#     test_bfs()

    # Bitpartite
#     test_bitpartite()


if __name__ == '__main__':
    main()
