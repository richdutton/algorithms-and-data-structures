# pylint:disable=W0212


class Node:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None

        self._balance_factor = 0
        self._height = 1

    def insert(self, key):
        assert key != self._key

        if key < self._key:
            if self._left is None:
                self._left = Node(key)
            else:
                self._left.insert(key)
        else:
            if self._right is None:
                self._right = Node(key)
            else:
                self._right.insert(key)

        self._update_balance_factor()
        self._update_height()

    def __contains__(self, key):
        if key == self._key:
            return True
        elif key < self._key:
            return False if self._left is None else key in self._left
        else:
            return False if self._right is None else key in self._right

    def _update_height(self):
        self._height = 1 + max(self._left._height if self._left is not None else 0,
                               self._right._height if self._right is not None else 0)

    def _update_balance_factor(self):
        self._balance_factor = ((self._right._height if self._right is not None else 0) -
                                (self._left._height if self._left is not None else 0))


class AVLTree:
    def __init__(self):
        self._root = None

    def insert(self, key):
        if not self._root:
            self._root = Node(key)
        else:
            self._root.insert(key)

    def __contains__(self, key):
        return False if self._root is None else key in self._root
