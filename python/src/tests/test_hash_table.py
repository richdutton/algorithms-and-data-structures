# pylint: disable=W0621
# pylint: disable=W0212

import pytest

from pkg.hash_table import HashTable, _INITIAL_ROW_COUNT

_KEY = 42
_VALUE = 'forty two'


@pytest.fixture
def empty_hash_table():
    return HashTable()


@pytest.fixture
def single_element_hash_table(empty_hash_table):
    hash_table = empty_hash_table
    hash_table[_KEY] = _VALUE

    return hash_table

# note: len tested variously by other tests


def test_init(empty_hash_table):
    assert len(empty_hash_table._rows) == _INITIAL_ROW_COUNT
    assert len(empty_hash_table) == 0

    for item in empty_hash_table._rows:
        assert item is None


def test_setitem(single_element_hash_table):
    assert len(single_element_hash_table._rows) == _INITIAL_ROW_COUNT
    assert len(single_element_hash_table) == 1

    found_something = False
    for row in single_element_hash_table._rows:
        if row:
            for cell in row:
                found_something = True
                assert cell == (42, 'forty two')

    assert found_something


def test_getitem(single_element_hash_table):
    value = single_element_hash_table[_KEY]

    assert value == _VALUE


def test_resize(empty_hash_table):
    hash_table = empty_hash_table

    # actual load factor to resize on could change but assume resizes by 1.0 at least
    # note: size of empty == _INITIAL_ROW_COUNT tested elsewhere
    for i in range(_INITIAL_ROW_COUNT):
        empty_hash_table[i] = i * 2

    assert len(hash_table) == _INITIAL_ROW_COUNT
    # actual multiplier could change but assume > _INITIAL_ROW_COUNT
    assert len(hash_table._rows) > _INITIAL_ROW_COUNT

    for i in range(_INITIAL_ROW_COUNT):
        assert empty_hash_table[i] == i * 2


if __name__ == '__main__':
    pytest.main()
