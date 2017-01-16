class _NilNode:
    def __init__(self, parent):
        self.parent = parent

    def find(self, key):
        return False


class _Node:
    def __init__(self, color, parent, key):
        self.color = color
        self.key = key
        self.parent = parent
        self.left = _NilNode(self)
        self.right = _NilNode(self)

    def find(self, key):
        if key == self.key:
            return True

        return self.left.find(key) if key < self.key else self.right.find(key)


class RedBlackTree:
    def __init__(self):
        self._root = _NilNode(self)

    def insert(self, key):
        if isinstance(self._root, _NilNode):
            self._root = _Node('black', None, key)
        else:

            potential_parent = self._root
            while True:
                if key == potential_parent.key:
                    raise KeyError()

                # todo: this should be on the potential parent
                insertion_point = 'left' if key < potential_parent.key else 'right'

                if isinstance(getattr(potential_parent, insertion_point), _NilNode):
                    setattr(potential_parent, insertion_point, _Node('red', potential_parent, key))
                    break
                else:
                    potential_parent = getattr(potential_parent, insertion_point)

    def __contains__(self, key):
        return self._root.find(key)

