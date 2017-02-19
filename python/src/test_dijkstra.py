# pylint:disable=W0621

import pytest

from .dijkstra import WeightedGraph, ConnectionAndWeight, PathAndCost, dijkstra_cost


@pytest.fixture
def grokking_weighted_graph():
    nodes = ['START', 'A', 'B', 'FINISH']
    connections = {}
    connections['START'] = [ConnectionAndWeight('A', 6), ConnectionAndWeight('B', 2)]
    connections['A'] = [ConnectionAndWeight('FINISH', 1)]
    connections['B'] = [ConnectionAndWeight('A', 3), ConnectionAndWeight('FINISH', 5)]

    return WeightedGraph(nodes, connections)


@pytest.fixture
def grokking_weighted_graph_large():
    nodes = ['BOOK', 'POSTER', 'RARE LP', 'BASS GUITAR', 'DRUM SET', 'PIANO']
    connections = {}
    connections['BOOK'] = [ConnectionAndWeight('POSTER', 0), ConnectionAndWeight('RARE LP', 5)]
    connections['POSTER'] = [ConnectionAndWeight('BASS GUITAR', 30), ConnectionAndWeight('DRUM SET', 35)]
    connections['RARE LP'] = [ConnectionAndWeight('BASS GUITAR', 15), ConnectionAndWeight('DRUM SET', 20)]
    connections['DRUM SET'] = [ConnectionAndWeight('PIANO', 10)]
    connections['BASS GUITAR'] = [ConnectionAndWeight('PIANO', 20)]

    return WeightedGraph(nodes, connections)


def test_dijkstra_grokking(grokking_weighted_graph):
    assert dijkstra_cost(grokking_weighted_graph, 'START', 'FINISH') == 6


def test_dijkstra_grokking_large(grokking_weighted_graph_large):
    assert dijkstra_cost(grokking_weighted_graph_large, 'BOOK', 'PIANO') == 35


if __name__ == '__main__':
    pytest.main()
