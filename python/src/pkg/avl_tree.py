# pylint:disable=W0212


class Node:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._height = 1

    def insert(self, key):
        assert key != self._key

        adjust_height = False
        if key < self._key:
            if self._left is None:
                self._left = Node(key)
                if self._right is None:
                    adjust_height = True
            else:
                if self._left.insert(key):
                    adjust_height = True
        else:
            if self._right is None:
                self._right = Node(key)
                if self._left is None:
                    adjust_height = True
            else:
                if self._right.insert(key):
                    adjust_height = True

        if adjust_height:
            self._height = 1 + max(self._left._calculate_height() if self._left is not None else 0,
                                   self._right._calculate_height() if self._right is not None else 0)

        return adjust_height

    @property
    def _balance_factor(self):
        return ((self._right._height if self._right is not None else 0) -
                (self._left._height if self._left is not None else 0))

    def __contains__(self, key):
        if key == self._key:
            return True
        elif key < self._key:
            return False if self._left is None else key in self._left
        else:
            return False if self._right is None else key in self._right

    def _calculate_height(self):
        height = 1 + max(self._left._calculate_height() if self._left is not None else 0,
                         self._right._calculate_height() if self._right is not None else 0)

        assert height == self._height
        return height

    def _calculate_balance_factor(self):
        balance_factor = ((self._right._calculate_height() if self._right is not None else 0) -
                          (self._left._calculate_height() if self._left is not None else 0))

        assert balance_factor == self._balance_factor
        return balance_factor


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
