# pylint: disable=C0103
# pylint: disable=W0621

from random import seed

import pytest

from pkg.merge_sort import merge_sort
from pkg.selection_sort import selection_sort
from pkg.quick_sort import quick_sort, in_place_quick_sort, quick_sort_iterative, quick_sort_alternate

seed(42)


@pytest.fixture(params=[merge_sort, selection_sort, quick_sort, in_place_quick_sort, quick_sort_iterative, quick_sort_alternate])
def sort(request):
    return request.param


def test_with_none_asserts(sort):
    with pytest.raises(AssertionError):
        sort(None)


def test_with_empty_returns_empty(sort):
    sorted_array = sort([])

    assert sorted_array == []


def test_with_single_element_returns_same(sort):
    array = [42]
    sorted_array = sort(array)

    assert sorted_array == array


def test_sorted_two_element_array_remains_sorted(sort):
    array = [21, 42]
    sorted_array = sort(array)

    assert sorted_array == array


def test_unsorted_two_element_array_is_sorted(sort):
    array = [84, 42]
    sorted_array = sort(array)

    assert sorted_array == sorted(array)


def test_unsorted_three_element_array_is_sorted(sort):
    array = [4, 2, 8]
    sorted_array = sort(array)

    assert sorted_array == sorted(array)


def test_large_unsorted_positive_array_is_sorted(sort):
    array = [14, 61, 98, 45, 75, 24, 85, 26, 27, 50, 21, 31, 3, 48, 12, 65, 39, 22, 22, 26, 10, 64, 82, 10, 31, 84, 26, 54, 34, 52]
    sorted_array = sort(array)

    assert sorted_array == sorted(array)


def test_move_pivot(sort):
    array = [1, 3, 2, 2]
    sorted_array = sort(array)
    assert sorted_array == sorted(array)


def test_large_unsorted_array_is_sorted(sort):
    array = [-89, 22, -94, 37, -54, -63, -79, -63, 39, 98, -58, 77, -40, 50, -61, -44, -77, 61, -43, -93, 57, 98, 26, -6, 34, -93, -11, -40, 65, -40]
    sorted_array = sort(array)

    assert sorted_array == sorted(array)


if __name__ == '__main__':
    pytest.main()
