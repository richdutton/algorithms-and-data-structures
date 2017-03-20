# pylint: disable=W0621
# pylint: disable=W0212
# pylint: disable=C0103

import pytest

from pkg.red_black_tree import _NilNode
from pkg.avl_tree import AVLTree
_TREE_TYPE = AVLTree

_DEFAULT_KEY = 42
_DEFAULT_KEY_2 = _DEFAULT_KEY * 2
_DEFAULT_KEY_3 = _DEFAULT_KEY_2 * 2
_DEFAULT_KEY_4 = _DEFAULT_KEY_3 * 2
# _DEFAULT_VALUE = 4.2


@pytest.fixture
def zero_element_tree():
    return _TREE_TYPE(rebalance=False)


@pytest.fixture
def one_element_tree(zero_element_tree):
    zero_element_tree.insert(_DEFAULT_KEY)
    return zero_element_tree


@pytest.fixture
def two_element_tree(one_element_tree):
    one_element_tree.insert(_DEFAULT_KEY_2)
    return one_element_tree


@pytest.fixture
def three_element_tree(two_element_tree):
    two_element_tree.insert(_DEFAULT_KEY_3)
    return two_element_tree


@pytest.fixture
def zero_element_rebalancing_tree():
    return _TREE_TYPE(rebalance=True)


def _insert_without_rebalance(tree, node):
    tree.insert(node)
    assert not _TREE_TYPE.rebalanced


def _insert_with_rebalance(tree, node):
    tree.insert(node)
    assert _TREE_TYPE.rebalanced


# TODO: permute insertions / set seed randomly as parameter to fixture
@pytest.fixture
def wikipedia_example_avl_tree_balanced(zero_element_rebalancing_tree):
    zero_element_tree = zero_element_rebalancing_tree
    tree = zero_element_tree
    for node in ['j', 'f', 'p', 'd', 'g', 'l', 'v', 'c', 'n', 's', 'x', 'q', 'u']:
        _insert_without_rebalance(tree, node)
    return tree


# todo: this should be less lenient for RedBlackTree
def assert_not_node(node):
    assert node is None or isinstance(node, _NilNode)


def test_zero_element_tree(zero_element_tree):
    assert_not_node(zero_element_tree.root)


def test_one_element_tree(one_element_tree):
    assert one_element_tree.root._key == _DEFAULT_KEY
    assert_not_node(one_element_tree.root._left)
    assert_not_node(one_element_tree.root._right)


def test_two_element_tree(two_element_tree):
    assert two_element_tree.root._key == _DEFAULT_KEY
    assert_not_node(two_element_tree.root._left)
    assert two_element_tree.root._right._key == _DEFAULT_KEY_2
    assert_not_node(two_element_tree.root._right._left)
    assert_not_node(two_element_tree.root._right._right)


def test_three_element_tree(three_element_tree):
    assert three_element_tree.root._key == _DEFAULT_KEY
    assert_not_node(three_element_tree.root._left)
    assert three_element_tree.root._right._key == _DEFAULT_KEY_2
    assert_not_node(three_element_tree.root._right._left)
    assert three_element_tree.root._right._right._key == _DEFAULT_KEY_3
    assert_not_node(three_element_tree.root._right._right._left)
    assert_not_node(three_element_tree.root._right._right._right)


def test_zero_element_tree_find_failure(zero_element_tree):
    assert _DEFAULT_KEY not in zero_element_tree


def test_one_element_tree_find_success(one_element_tree):
    assert _DEFAULT_KEY in one_element_tree


def test_one_element_tree_find_failure(one_element_tree):
    assert _DEFAULT_KEY_2 not in one_element_tree


def test_two_element_tree_find_success(two_element_tree):
    assert _DEFAULT_KEY in two_element_tree
    assert _DEFAULT_KEY_2 in two_element_tree


def test_two_element_tree_find_failure(two_element_tree):
    assert _DEFAULT_KEY_3 not in two_element_tree


def test_three_element_tree_find_success(three_element_tree):
    assert _DEFAULT_KEY in three_element_tree
    assert _DEFAULT_KEY_2 in three_element_tree
    assert _DEFAULT_KEY_3 in three_element_tree


def test_three_element_tree_find_failure(three_element_tree):
    assert _DEFAULT_KEY_4 not in three_element_tree


# https://en.wikipedia.org/wiki/AVL_tree
def test_wikipedia_example_avl_tree_balanced_is_balanced(wikipedia_example_avl_tree_balanced):
    tree = wikipedia_example_avl_tree_balanced

    assert tree.root._key == 'j'
    assert tree.root._left._key == 'f'
    assert tree.root._right._key == 'p'
    assert tree.root._left._left._key == 'd'
    assert tree.root._left._right._key == 'g'
    assert tree.root._right._left._key == 'l'
    assert tree.root._right._right._key == 'v'
    assert tree.root._left._left._left._key == 'c'
    assert tree.root._right._left._right._key == 'n'
    assert tree.root._right._right._left._key == 's'
    assert tree.root._right._right._right._key == 'x'
    assert tree.root._right._right._left._left._key == 'q'
    assert tree.root._right._right._left._right._key == 'u'


def test_wikipedia_example_avl_tree_balanced_heights(wikipedia_example_avl_tree_balanced):
    tree = wikipedia_example_avl_tree_balanced

    assert tree.root._height == 5
    assert tree.root._left._height == 3
    assert tree.root._right._height == 4
    assert tree.root._left._left._height == 2
    assert tree.root._left._right._height == 1
    assert tree.root._right._left._height == 2
    assert tree.root._right._right._height == 3
    assert tree.root._left._left._left._height == 1
    assert tree.root._right._left._right._height == 1
    assert tree.root._right._right._left._height == 2
    assert tree.root._right._right._right._height == 1
    assert tree.root._right._right._left._left._height == 1
    assert tree.root._right._right._left._right._height == 1


# balance_factors inverted vs. wikipedia page, per MIT method
def test_wikipedia_example_avl_tree_balanced_balance_factors(wikipedia_example_avl_tree_balanced):
    tree = wikipedia_example_avl_tree_balanced

    assert tree.root._balance_factor == -1
    assert tree.root._left._balance_factor == 1
    assert tree.root._right._balance_factor == -1
    assert tree.root._left._left._balance_factor == 1
    assert tree.root._left._right._balance_factor == 0
    assert tree.root._right._left._balance_factor == -1
    assert tree.root._right._right._balance_factor == 1
    assert tree.root._left._left._left._balance_factor == 0
    assert tree.root._right._left._right._balance_factor == 0
    assert tree.root._right._right._left._balance_factor == 0
    assert tree.root._right._right._right._balance_factor == 0
    assert tree.root._right._right._left._left._balance_factor == 0
    assert tree.root._right._right._left._right._balance_factor == 0


def _assert_node(element, key, height, balance_factor):
    assert element._key == key
    assert element._height == height
    assert element._balance_factor == balance_factor


# todo: use or modify existing fixtures
def test_simple_right_rotation(zero_element_rebalancing_tree):
    zero_element_tree = zero_element_rebalancing_tree
    _insert_without_rebalance(zero_element_tree, 3)
    _insert_without_rebalance(zero_element_tree, 2)
    _insert_with_rebalance(zero_element_tree, 1)
    _assert_node(zero_element_tree.root, 2, 2, 0)
    _assert_node(zero_element_tree.root._left, 1, 1, 0)
    _assert_node(zero_element_tree.root._right, 3, 1, 0)


def test_right_rotation_under_parent(zero_element_rebalancing_tree):
    zero_element_tree = zero_element_rebalancing_tree
    _insert_without_rebalance(zero_element_tree, 4)
    _insert_without_rebalance(zero_element_tree, 3)
    _insert_without_rebalance(zero_element_tree, 5)
    _insert_without_rebalance(zero_element_tree, 2)
    _insert_with_rebalance(zero_element_tree, 1)
    _assert_node(zero_element_tree.root, 4, 3, 1)
    _assert_node(zero_element_tree.root._left, 2, 2, 0)
    _assert_node(zero_element_tree.root._right, 5, 1, 0)
    _assert_node(zero_element_tree.root._left._left, 1, 1, 0)
    _assert_node(zero_element_tree.root._left._right, 3, 1, 0)


# https://www.quora.com/Why-is-it-that-rebalancing-nodes-in-an-AVL-tree-may-trickle-up-so-that-nodes-at-higher-nodes-need-to-be-fixed-too
def test_quora_right_rotation_with_subtrees(zero_element_rebalancing_tree):
    zero_element_tree = zero_element_rebalancing_tree
    _insert_without_rebalance(zero_element_tree, 20)
    _insert_without_rebalance(zero_element_tree, 10)
    _insert_without_rebalance(zero_element_tree, 30)
    _insert_without_rebalance(zero_element_tree, 5)
    _insert_without_rebalance(zero_element_tree, 15)
    _insert_with_rebalance(zero_element_tree, 9)
    _assert_node(zero_element_tree.root, 10, 3, 0)
    _assert_node(zero_element_tree.root._left, 5, 2, -1)
    _assert_node(zero_element_tree.root._right, 20, 2, 0)
    _assert_node(zero_element_tree.root._left._right, 9, 1, 0)
    _assert_node(zero_element_tree.root._right._left, 15, 1, 0)
    _assert_node(zero_element_tree.root._right._right, 30, 1, 0)

# def test_simple_left_rotation(zero_element_tree):
#     zero_element_tree.insert(1)
#     zero_element_tree.insert(2)
#     zero_element_tree.insert(3)
    # import pdb; pdb.set_trace()


if __name__ == '__main__':
    pytest.main()
