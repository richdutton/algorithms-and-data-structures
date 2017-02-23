# pylint: disable=E1133

from collections import namedtuple

_INITIAL_ROW_COUNT = 16
_RESIZE_AT_LOAD_FACTOR = 0.7
_SCALING_FACTOR = 2

_Item = namedtuple('_Item', 'key value')


class HashTable:
    def __init__(self):
        self._rows = [None] * _INITIAL_ROW_COUNT
        self._len = 0

    @property
    def _row_count(self):
        return len(self._rows)

    def __getitem__(self, key):
        row_index = row_index = hash(key) % self._row_count
        row = self._rows[row_index]
        for item in row:
            if item.key == key:
                return item.value

        raise KeyError()

    @staticmethod
    def _set_item_on_rows(rows, key, value):
        row_index = hash(key) % len(rows)

        if not rows[row_index]:
            assert rows[row_index] is None
            rows[row_index] = []

        # using a tree here would be faster
        rows[row_index].append(_Item(key, value))

    def _resize(self):
        new_row_count = self._row_count * _SCALING_FACTOR
        new_rows = [None] * new_row_count

        for row in self._rows:
            if row:
                for cell in row:
                    self._set_item_on_rows(new_rows, cell.key, cell.value)

        self._rows = new_rows

    def __setitem__(self, key, value):
        new_load_factor = (self._len + 1) / self._row_count
        if new_load_factor >= _RESIZE_AT_LOAD_FACTOR:
            self._resize()

        self._set_item_on_rows(self._rows, key, value)
        self._len += 1

    def __len__(self):
        return self._len
