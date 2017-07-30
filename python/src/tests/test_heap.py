# pylint:disable=W0621, C0103, W0212

from pkg.heap import Heap

import pytest

_ITEMS = [42, 84, 168]
# test size increase
# test inserted item inserted & test heap sorted - probably add a few items and assert each time


@pytest.fixture
def _zero_element_heap():
    return Heap()


@pytest.fixture
def _single_element_heap(_zero_element_heap):
    _zero_element_heap.insert(_ITEMS[0])
    return _zero_element_heap


@pytest.fixture
def _three_element_heap_added_in_order(_zero_element_heap):
    import pdb; pdb.set_trace()
    for item in _ITEMS:
        _zero_element_heap.insert(item)

    return _zero_element_heap


@pytest.fixture
def _three_element_heap_added_reverse_order(_zero_element_heap):
    for item in reversed(_ITEMS):
        _zero_element_heap.insert(item)

    return _zero_element_heap


def test_zero_element_heap(_zero_element_heap):
    assert len(_zero_element_heap) == 0
    assert len(_zero_element_heap._array) != 0


def test_one_element_heap(_single_element_heap):
    assert len(_single_element_heap) == 1
    assert _single_element_heap._array[0] == 42


def test_three_element_heap_added_in_order(_three_element_heap_added_in_order):
    import pdb; pdb.set_trace()
