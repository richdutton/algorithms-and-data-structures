# pylint: disable=W0621
# pylint: disable=W0212
# pylint: disable=C0103

import pytest

from pkg.red_black_tree import RedBlackTree, _NilNode

_DEFAULT_KEY = 42
_DEFAULT_KEY_2 = _DEFAULT_KEY * 2
_DEFAULT_KEY_3 = _DEFAULT_KEY_2 * 2
_DEFAULT_KEY_4 = _DEFAULT_KEY_3 * 2
# _DEFAULT_VALUE = 4.2


@pytest.fixture
def zero_element_tree():
    return RedBlackTree()


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


def test_zero_element_tree(zero_element_tree):
    assert isinstance(zero_element_tree._root, _NilNode)


def test_one_element_tree(one_element_tree):
    assert one_element_tree._root.key == _DEFAULT_KEY
    assert isinstance(one_element_tree._root.left, _NilNode)
    assert isinstance(one_element_tree._root.right, _NilNode)


def test_two_element_tree(two_element_tree):
    assert two_element_tree._root.key == _DEFAULT_KEY
    assert isinstance(two_element_tree._root.left, _NilNode)
    assert two_element_tree._root.right.key == _DEFAULT_KEY_2
    assert isinstance(two_element_tree._root.right.left, _NilNode)
    assert isinstance(two_element_tree._root.right.right, _NilNode)


def test_three_element_tree(three_element_tree):
    assert three_element_tree._root.key == _DEFAULT_KEY
    assert isinstance(three_element_tree._root.left, _NilNode)
    assert three_element_tree._root.right.key == _DEFAULT_KEY_2
    assert isinstance(three_element_tree._root.right.left, _NilNode)
    assert three_element_tree._root.right.right.key == _DEFAULT_KEY_3
    assert isinstance(three_element_tree._root.right.right.left, _NilNode)
    assert isinstance(three_element_tree._root.right.right.right, _NilNode)


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


if __name__ == '__main__':
    pytest.main()
