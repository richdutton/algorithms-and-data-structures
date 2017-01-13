# pylint: disable=W0621
# pylint: disable=W0212
# pylint: disable=C0103

import pytest

from .red_black_tree import RedBlackTree

_DEFAULT_KEY = 42
_DEFAULT_VALUE = 4.2


@pytest.fixture
def zero_element_tree():
    return RedBlackTree()


@pytest.fixture
def one_element_tree(zero_element_tree):
    zero_element_tree.insert(_DEFAULT_KEY, _DEFAULT_VALUE)
    return zero_element_tree


@pytest.fixture
def two_element_tree(one_element_tree):
    one_element_tree.insert(_DEFAULT_KEY * 2, _DEFAULT_VALUE * 2)
    return one_element_tree


def test_zero_element_tree(zero_element_tree):
    assert zero_element_tree.left is None
    assert zero_element_tree.right is None


def test_one_element_tree(one_element_tree):
    assert one_element_tree.left is None or one_element_tree.right is None
    assert one_element_tree.left is not None or one_element_tree.right is not None

    not_none = one_element_tree.left if one_element_tree.left is not None else one_element_tree.right
    assert not_none.key == _DEFAULT_KEY
    assert not_none._value == _DEFAULT_VALUE


def test_zero_element_tree_find(zero_element_tree):
    assert not zero_element_tree.find(_DEFAULT_KEY)


def test_one_element_tree_find_success(one_element_tree):
    assert one_element_tree.find(_DEFAULT_KEY)


def test_one_element_tree_find_failure(one_element_tree):
    assert not one_element_tree.find(_DEFAULT_KEY * 2)


def test_two_element_tree_find_success(two_element_tree):
    assert two_element_tree.find(_DEFAULT_KEY)
    assert two_element_tree.find(_DEFAULT_KEY * 2)
