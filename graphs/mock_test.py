import mock
import unittest
from directed_graph_list import DirectedGraph


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.dg = DirectedGraph()
        self.dg.add_edge(0, 1)
        self.dg.add_edge(0, 5)
        self.dg.add_edge(1, 2)
        self.dg.add_edge(2, 4)
        self.dg.add_edge(2, 6)
        self.dg.add_edge(3, 2)
        self.dg.add_edge(5, 8)
        self.dg.add_edge(6, 5)
        self.dg.add_edge(7, 5)

        self.dg2 = DirectedGraph()
        self.dg2.add_edge(0, 2)
        self.dg2.add_edge(1, 3)
        self.dg2.add_edge(3, 2)
        self.dg2.add_edge(2, 1)
        self.dg2.add_edge(4, 5)
        self.dg2.add_edge(5, 6)
        self.dg2.add_edge(6, 4)
        self.dg2.add_edge(3, 5)
        self.dg2.add_edge(7, 5)
        self.dg2.add_edge(8, 10)
        self.dg2.add_edge(10, 11)
        self.dg2.add_edge(11, 9)
        self.dg2.add_edge(9, 8)

    def test_bfs(self):
        expected_output = {1: 0, 5: 0, 2: 1, 8: 5, 4: 2, 6: 2}
        self.assertEqual(self.dg.bfs(), expected_output)

    def test_dfs(self):

        expected_output = {1: 0, 5: 0, 8: 5, 2: 1, 4: 2, 6: 2}

        c1, p1 = self.dg.dfs()
        self.assertEqual(p1, expected_output)

    def test_toplogical_sort(self):
        expected_output = [7, 3, 0, 1, 2, 4, 6, 5, 8]
        self.assertEqual(self.dg.topological_sort(), expected_output)

    def test_strongly_connected_components(self):
        expected_output = [[10, 11, 9, 8], [7], [0], [1, 3, 2], [6, 4, 5]]
        self.assertEqual(self.dg2.strongly_connected_components(), expected_output)


def main():
    """docstring for main"""
    unittest.main()


if __name__ == '__main__':
    main()

