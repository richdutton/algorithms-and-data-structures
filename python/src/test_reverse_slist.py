# pylint:disable=W0621

import pytest

from .reverse_slist import reverse_slist, Node


@pytest.fixture
def _one_node():
    return Node(42, None)


@pytest.fixture
def _two_nodes(_one_node):
    two_nodes = _one_node
    two_nodes.next_ = Node(84, None)
    return two_nodes


@pytest.fixture
def _three_nodes(_two_nodes):
    three_nodes = _two_nodes
    three_nodes.next_.next_ = Node(168, None)
    return three_nodes


def _slist_to_array(node):
    array = [node.value]
    while node.next_ is not None:
        node = node.next_
        array.append(node.value)

    return array


def test_one_node(_one_node):
    reversed_ = reverse_slist(_one_node)
    assert _slist_to_array(reversed_) == [42]


def test_two_nodes(_two_nodes):
    reversed_ = reverse_slist(_two_nodes)
    assert _slist_to_array(reversed_) == [84, 42]


def test_three_nodes(_three_nodes):
    reversed_ = reverse_slist(_three_nodes)
    assert _slist_to_array(reversed_) == [168, 84, 42]
