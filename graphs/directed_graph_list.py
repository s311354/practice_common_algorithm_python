import queue
import copy


class DirectedGraph(object):
    """docstring for ClassName"""

    def __init__(self):
        # class dict(** kwargs): Return a new dictionary initialized from an
        # optional position argument and a possible empty set of keyword arguments.
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        """docstring for add_edge"""
        """ Adds an edge defined by vertices source and destination

        @param param: source
        @param param: destination

        @return:  Description
        """
        if source not in self.adjacency_list:
            self.adjacency_list[source] = set()
        # {vertex, {neighbor, ...} }
        self.adjacency_list[source].add(destination)

    def get_vertex(self):
        """docstring for get_vertes"""
        """ Generator for returning the next vertex from the adjacency list

        @rtype :  Type

        """
        for v in self.adjacency_list:
            yield v

    def get_neighbor(self, vertex):
        """docstring for get_neighbor"""
        """ Generator for returning the next vertex adjacency to the given vertex

        @param param:  vertex
        """
        if vertex in self.adjacency_list:
            for u in self.adjacency_list[vertex]:
                yield u

    def get_reverse_neighbor(self, vertex):
        """docstring for get_reverse_neighbor"""
        """ Generator for returning the reversed edge neighbor to the given vertex (parent)

        @param param:  vertex
        """
        reversed_list = {}
        for v, u in self.adjacency_list.items():
            for w in u:
                if w not in reversed_list:
                    reversed_list[w] = set()
                reversed_list[w].add(v)

        if vertex in reversed_list:
            for u in reversed_list[vertex]:
                yield u

    def dfs(self):
        """docstring for dfs"""
        """ Computes the initial source vertices for each connected component
        and the parents for each vertex as determined through depth-first-search

        @return:  initial soruce vertices for each connected component, parents for each vertex
        @rtype :  set, dict
        """
        parents = {}
        components = set()
        to_visit = []

        for vertex in self.get_vertex():
            if vertex not in parents:
                components.add(vertex)
            else:
                continue

            to_visit.append(vertex)

            while to_visit:
                v = to_visit.pop()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.append(neighbor)

        return components, parents

    def bfs(self):
        """docstring for bfs"""
        """ Computes the parents for each vertex as determined through breath-first search

        @return:  parents for each vertex
        @rtype :  dict
        """
        parents = {}
        to_visit = queue.Queue()

        for vertex in self.get_vertex():
            to_visit.put(vertex)

            while not to_visit.empty():
                v = to_visit.get()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.put(neighbor)

        return parents

    def contain_cycle(self):
        """docstring for contain_cycle"""
        """ Determines if one of the connected compents contains a cycle

        @return:  true if one of the connected compents contains a cycle
        @rtype :  bool
        """
        contains_cycle = False
        STATUS_STARTED = 1
        STATUS_FINISHED = 2

        for vertex in self.get_vertex():
            statuses = {}
            # BFS (queue)
            to_visit = [vertex]

            while to_visit and not contains_cycle:
                v = to_visit.pop()

                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED

                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)

                for u in self.get_neighbor(v):
                    if u in statuses:
                        if statuses[u] == STATUS_STARTED:
                            contains_cycle = True
                            break
                    else:
                        to_visit.append(u)

                if contains_cycle:
                    break

        return contains_cycle

    def topological_sort(self):
        """docstring for topological_sort"""
        """ Determines the priority of vertices to be visited.
        " Kahn's algorithm

        @return:  Description
        """
        STATUS_STARTED = 1
        STATUS_FINISHED = 2

        order = []
        statuses = {}

        assert(not self.contain_cycle())

        for vertex in self.get_vertex():
            to_visit = [vertex]

            while to_visit:
                v = to_visit.pop()

                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED
                        order.append(v)
                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)

                for u in self.get_neighbor(v):
                    if u not in statuses:
                        to_visit.append(u)
        order.reverse()

        return order

    def dfs_reverse(self, vertex, component, visited):
        """docstring for dfs_reverse"""
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            for u in self.get_reverse_neighbor(vertex):
                self.dfs_reverse(u, component, visited)

    def scc_dfs_forward_pass(self, stack):
        """docstring for scc_dfs_forward_pass"""
        components = []
        # class set([iterable]) : return a new set or forzenset object whose elements are taken from iterable. The elements of a set must be hashable. To represent sets of sets, the inner sets must be forzenset objects. If iterable is not specified, a new empty set is returned.
        visited = set()

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                self.dfs_reverse(v, component, visited)
                component.reverse()
                components.append()

        return components

    def dfs_forward(self, vertex, stack, visited):
        """docstring for dfs_forward"""
        if vertex not in visited:
            visited.add(vertex)
            for u in self.get_neighbor(vertex):
                self.dfs_forward(u, stack, visited)
            stack.append(vertex)

    def scc_dfs_reverse_pass(self, stack):
        """docstring for scc_dfs_reverse_pass"""
        components = []
        visited = set()

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                self.dfs_reverse(v, component, visited)
                component.reverse()
                components.append(component)

        return components

    def strongly_connected_components(self):
        """docstring for strongly_connected_components"""
        """ Compute the vertices in the strongly connected compents

        @return:  list of lists, one for each compents's vertices
        """
        stack = self.scc_dfs_forward_pass()
        compents = self.scc_dfs_reverse_pass(stack)

        return compents


def get_test_graph_1():
    """docstring for get_test_graph_1"""
    dg = DirectedGraph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 5)
    dg.add_edge(1, 2)
    dg.add_edge(2, 4)
    dg.add_edge(2, 6)
    dg.add_edge(3, 2)
    dg.add_edge(5, 8)
    dg.add_edge(6, 5)
    dg.add_edge(7, 5)

    return dg


def get_test_graph_2():
    """docstring for get_test_graph_2"""
    dg_small = DirectedGraph()
    dg_small.add_edge(2, 1)
    dg_small.add_edge(4, 5)
    dg_small.add_edge(0, 1)
    dg_small.add_edge(1, 4)
    dg_small.add_edge(1, 3)

    return dg_small


def get_test_graph_3():
    """docstring for get_test_graph_3"""
    dg_other = DirectedGraph()
    dg_other.add_edge(3, 11)
    dg_other.add_edge(5, 2)
    dg_other.add_edge(2, 4)
    dg_other.add_edge(2, 7)
    dg_other.add_edge(8, 11)
    dg_other.add_edge(4, 7)
    dg_other.add_edge(7, 8)

    return dg_other


def test_dfs():
    """docstring for test_dfs"""
    dg1 = get_test_graph_1()
    c1, p1 = dg1.dfs()
    assert(p1 == {1: 0, 5: 0, 8: 5, 2: 1, 4: 2, 6: 2})


def test_bfs():
    """docstring for fname"""
    dg1 = get_test_graph_1()
    p1 = dg1.bfs()
    assert(p1 == {1: 0, 5: 0, 2: 1, 8: 5, 4: 2, 6: 2})

## Need to understand how topological sort work
def test_topological_sort():
    """docstring for test_topological_sort"""
    assert (get_test_graph_1().topological_sort() == [7, 3, 0, 1, 2, 4, 6, 5, 8] )
#     assert (get_test_graph_2().topological_sort() == [2, 0, 1, 3, 4, 5])
#     assert (get_test_graph_3().topological_sort() == [5, 3, 2, 4, 7, 8, 11])


def main():
    """docstring for main"""
    test_dfs()
    test_bfs()
    test_topological_sort()


if __name__ == '__main__':
    main()
