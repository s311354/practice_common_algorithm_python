import mock
import unittest
from directed_graph_list import DirectedGraph


class TestMethods(unittest.TestCase):

    def test_bfs(self):
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

        expected_output = {1: 0, 5: 0, 2: 1, 8: 5, 4: 2, 6: 2}
        self.assertEqual(dg.bfs(), expected_output)

    def test_dfs(self):
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

        expected_output = {1: 0, 5: 0, 8: 5, 2: 1, 4: 2, 6: 2}

        c1, p1 = dg.dfs()
        self.assertEqual(p1, expected_output)

    def test_toplogical_sort(self):
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

        expected_output = [7, 3, 0, 1, 2, 4, 6, 5, 8]
        self.assertEqual(dg.topological_sort(), expected_output)

    def test_strongly_connected_components(self):
        dg = DirectedGraph()
        dg.add_edge(0, 2)
        dg.add_edge(1, 3)
        dg.add_edge(3, 2)
        dg.add_edge(2, 1)
        dg.add_edge(4, 5)
        dg.add_edge(5, 6)
        dg.add_edge(6, 4)
        dg.add_edge(3, 5)
        dg.add_edge(7, 5)
        dg.add_edge(8, 10)
        dg.add_edge(10, 11)
        dg.add_edge(11, 9)
        dg.add_edge(9, 8)

        expected_output = [[10, 11, 9, 8], [7], [0], [1, 3, 2], [6, 4, 5]]
        self.assertEqual(dg.strongly_connected_components(), expected_output)


def main():
    """docstring for main"""
    unittest.main()


if __name__ == '__main__':
    main()

