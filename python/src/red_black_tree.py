class _NilNode:
    def __init__(self, parent):
        self.parent = parent

    def __contains__(self, _):
        return False


class _Node:
    def __init__(self, color, parent, key):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = _NilNode(self)
        self.right = _NilNode(self)

    def __contains__(self, key):
        if key == self.key:
            return True

        return key in self.left if key < self.key else key in self.right

    def insert(self, key):
        if key == self.key:
            raise KeyError()

        insertion_point = 'left' if key < self.key else 'right'

        if isinstance(getattr(self, insertion_point), _NilNode):
            setattr(self, insertion_point, _Node('red', self, key))
        else:
            getattr(self, insertion_point).insert(key)


class RedBlackTree:
    def __init__(self):
        self._root = _NilNode(self)

    def insert(self, key):
        if isinstance(self._root, _NilNode):
            self._root = _Node('black', None, key)
        else:
            self._root.insert(key)

    def __contains__(self, key):
        return key in self._root

