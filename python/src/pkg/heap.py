_INITIAL_SIZE = 8
_RESIZE_FACTOR = 2


class Heap:
    def __init__(self):
        self._array = [None] * _INITIAL_SIZE
        self._len = 0

    def __len__(self):
        return self._len

    """ peek item """
    def __getitem__(self):
        # todo:
        pass

    def _increase_size(self):
        array = [None] * len(self._array) * _RESIZE_FACTOR
        for index, item in self._array:
            array[index] = item

        self._array = array

    @staticmethod
    def _left_child_index(index):
        return index * 2 + 1

    @staticmethod
    def _right_child_index(index):
        return index * 2 + 2

    @staticmethod
    def _parent_index(index):
        return (index - 1) // 2

    def insert(self, item):
        if len(self) == len(self._array):
            self._increase_size()

        self._array[len(self)] = item
        self._len += 1

        for index in range(self._len -1, 0, -1):
            parent_index = self._parent_index(index)
            if self._array[index] > self._array[parent_index]:
                self._array[index], self._array[parent_index] = self._array[parent_index], self._array[index]
            else:
                break
