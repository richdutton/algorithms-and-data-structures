import random


class RedBlackTreeNode:
    def __init__(self, color='black', key=None, value=None):
        self._color = color
        self.key = key
        self._value = value
        self.left = None
        self.right = None

        self.assert_valid()

    def assert_valid(self):
        assert self._color in ('black', 'red')

        if self.key is None:
            assert self._value is None
            assert self.left is None
            assert self.right is None
            assert self._color is 'black'


class RedBlackTree:
    def __init__(self):
        self.left = None
        self.right = None

    def assert_valid(self):
        pass

    def insert(self, key, value):
        potential_parent = self

        while True:
            left_or_right = random.choice(('left', 'right'))
            if potential_parent.__dict__[left_or_right] is None:
                potential_parent.__dict__[left_or_right] = RedBlackTreeNode('black', key, value)
                potential_parent.assert_valid()
                break
            potential_parent = left_or_right

    def _find(self, node, key):
        if node is None:
            return False

        if self._find(node.left, key):
            return True

        if node != self and node.key == key:
            return True

        if self._find(node.right, key):
            return True

        return False

    def find(self, key):
        return self._find(self, key)
