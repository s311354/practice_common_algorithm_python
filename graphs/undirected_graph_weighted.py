import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeight(object):
    """docstring for GraphUndirectedWeight"""

    def __init__(self, vertex_count):
        # initialize list
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        """docstring for add_edge"""
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_neighbor(self, vertex):
        """Returns the next neighbor to vertex

        @param param:  vertex
        @rtype :  Edge

        """
        for elem in self.adjacency_list[vertex]:
            yield elem

    def get_vertex(self):
        """docstring for get_vertex"""
        for item in range(self.vertex_count):
            yield item

    # Dijkstra's Algorithm
    def dijkstra(self, source, dest):
        """docstring for dijkstra"""
        """ Dijkstra's Algorithm

            Dijkstra's algorithm allows us to find the
            shortest path between any two vertices of a graph.
        """
        q = queue.PriorityQueue()
        parents = []
        distance = []
        start_weight = float("inf")

        for item in self.get_vertex():
            weight = start_weight
            if source == item:
                weight = 0

            distance.append(weight)
            parents.append(None)

        q.put(([0, source]))

        # Short Distance
        while not q.empty():
            v_tuple = q.get()
            node = v_tuple[1]

            for next_node in self.get_neighbor(node):
                candidate_distance = distance[node] + next_node.weight

                if distance[next_node.vertex] > candidate_distance:
                    distance[next_node.vertex] = candidate_distance
                    parents[next_node.vertex] = node

                    # # primitive but effective negative cycle detection
                    if candidate_distance < -1000:
                        raise Exception("Negative cycle detected")

                    q.put(([distance[next_node.vertex], next_node.vertex]))

        # Short Path
        shortest_path = []
        end = dest
        while end is not None:
            shortest_path.append(end)
            end = parents[end]

        shortest_path.reverse()

        return shortest_path, distance[dest]

    def prim(self):
        """docstring for prim"""
        """Description
        Returns a dictionary of parents of vertices in a minimum spanning tree
        @rtype :  dict
        """
        s = set()
        q = queue.PriorityQueue()
        parents = {}
        start_weight = float("inf")
        weights = {}

        for item in self.get_vertex():
            weight = start_weight
            if item == 0:
                q.put(([0, item]))
            weights[item] = weight
            parents[item] = None

        while not q.empty():
            v_tuple = q.get()
            vertex = v_tuple[1]

            s.add(vertex)

            for node in self.get_neighbor(vertex):
                if node.vertex not in s:
                    if node.weight < weights[node.vertex]:
                        parents[node.vertex] = vertex
                        weights[node.vertex] = node.weight
                        q.put(([node.weight, node.vertex]))

        return parents


def main():
    """docstring for main"""
    g = GraphUndirectedWeight(9)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 7, 6)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 7, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 6, 1)
    g.add_edge(6, 7, 2)
    g.add_edge(6, 8, 2)
    g.add_edge(7, 8, 2)

    shortest_path, distance = g.dijkstra(0, 1)
    assert shortest_path == [0, 1] and distance == 4

    shortest_path, distance = g.dijkstra(0, 8)
    assert shortest_path == [0, 1, 2, 3, 7, 8] and distance == 11
    print("The Shortest path from source 0 to destionation 8 is", distance)

    msp = g.prim()
    print(msp)

    assert (msp == {0: None, 1: 0, 2: 1, 3: 2, 4: 5, 5: 3, 6: 5, 7: 3, 8: 6})


if __name__ == '__main__':
    main()
