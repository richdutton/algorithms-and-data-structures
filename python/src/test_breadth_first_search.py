# pylint:disable=W0621
# pylint:disable=C0103

from collections import defaultdict
import subprocess
import random

import pygraphviz as pgv
import pytest

from .breadth_first_search import Graph, simple_breadth_first_search, tracking_breadth_first_search, alternating_breadth_first_search

random.seed(42)

_SMALL_NUMBER_OF_NODES = 10
_LARGE_NUMBER_OF_NODES = 20
_LIKELIHOOD_OF_CONNECTION_BETWEEN_GIVEN_NODES = 0.2
_NODE_1 = 2
_NODE_2 = 3


def _graph_of_size(size):
    nodes = range(size)
    connections = defaultdict(list)
    for index_1, node_1 in enumerate(nodes):
        for node_2, node_2 in enumerate(nodes[index_1:]):
            if node_1 != node_2 and random.random() < _LIKELIHOOD_OF_CONNECTION_BETWEEN_GIVEN_NODES:
                connections[node_1] += [node_2]
                connections[node_2] += [node_1]

    return Graph(nodes, connections)


@pytest.fixture(scope='module')
def large_graph():
    random.seed(42)
    return _graph_of_size(_LARGE_NUMBER_OF_NODES)


# with the seed 42, we will get the following Graph
# strict graph "" {
# 	0 -- 2;
# 	0 -- 8;
# 	2 -- 5;
# 	2 -- 9;
# 	8 -- 9;
# 	1 -- 2;
# 	1 -- 5;
# 	1 -- 6;
# 	6 -- 9;
# 	3 -- 6;
# 	3 -- 7;
# 	4;
# }
@pytest.fixture(scope='module')
def small_graph():
    random.seed(42)
    return _graph_of_size(_SMALL_NUMBER_OF_NODES)


def graph_to_a_graph(graph):
    a_graph = pgv.AGraph()
    for node in graph.nodes:
        a_graph.add_node(node)
        for connected_node in graph.connections[node]:
            # todo: we'll add nodes twice but whatever
            a_graph.add_edge(node, connected_node)

    return a_graph


def save_a_graph(a_graph):
    a_graph.write('large.dot')
    a_graph.layout()
    a_graph.draw('large.png')
    subprocess.Popen(['open', './large.png'])


def test_convert_and_save_graph():
    a_graph = graph_to_a_graph(large_graph())
    save_a_graph(a_graph)


def test_simple_breadth_first_search_success(small_graph):
    assert simple_breadth_first_search(small_graph, _NODE_1, _NODE_2)


def test_tracking_breadth_first_search_success(small_graph):
    path = tracking_breadth_first_search(small_graph, _NODE_1, _NODE_2)
    assert path == [2, 1, 6, 3]


def test_alternating_breadth_first_search_success(large_graph):
    assert simple_breadth_first_search(large_graph, _NODE_1, _NODE_2)
    assert alternating_breadth_first_search(large_graph, _NODE_1, _NODE_2)
    import pdb; pdb.set_trace()
