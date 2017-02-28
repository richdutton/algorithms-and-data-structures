# pylint:disable=C0103


class _NilNode:
    def __init__(self, parent):
        self.parent = parent

    def __contains__(self, _):
        return False


# todo: name key, rather than _key, is incompatible with tests. ditto left and right
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

    # def rebalance_case_1(self, n, p, g, u):
    #     pass

    # def _rebalance(self):
    #     n = self
    #     # case 0
    #     if n == self.tree._root:
    #         n.color = 'black
    #         return

    #     p = n.parent
    #     n_insertion_point = 'left' if n == p.left else 'right'

    #     g = p.parent
    #     u = None
    #     if g is not None:
    #         u_insertion_point = 'right' if p == g.left else 'left'
    #         u = getattr(g, u_insertion_point)

    #         # case 1
    #         if u.color == 'red':
    #             assert g.color == 'black'
    #             g.color = 'red'
    #             assert p.color == 'red'
    #             assert u.color == 'red'
    #             p.color = 'black'
    #             u.color = 'black'

    #             g._rebalance()
    #             return

    def insert(self, key):
        if key == self.key:
            raise KeyError()

        insertion_point = 'left' if key < self.key else 'right'

        if isinstance(getattr(self, insertion_point), _NilNode):
            n = _Node('red', self, key)
            setattr(self, insertion_point, n)
            # easier to go with the wikipedia code than the below
            # n._rebalance()
        else:
            getattr(self, insertion_point).insert(key)


class RedBlackTree:
    def __init__(self):
        self._root = _NilNode(None)

    def insert(self, key):
        if isinstance(self._root, _NilNode):
            self._root = _Node('black', None, key)
        else:
            self._root.insert(key)

    def __contains__(self, key):
        return key in self._root

# Case 0?
# In the special case that where the _root is red, we can always just turn it black to satisfy property 2, without violating the other constraints.

# Case 1
# If U is red, we can just toggle the colors of P, U, and G. Flip G from black to red. Flip P and U from red to black. We haven't changed the number of black
# nodes in any path.
# However, by making G red, we might have created a red violation with G's parent. If so, we recursively apply the full logic to handle a red violation,
# where this G becomes the new N.

# Case 2
# Case A (N and P are both left children)
# C becomes left child of G (which was Nil); G becomes right child of P (where C was);
# P goes black and G goes red
#
# Case B (P is a left child, and N is a right child)
# b becomes the right child of P; P becomes the left child of N; C becomes the left child of G; G becomes the right child of N
# N becomes black; G becomes red

# Case C (mirror of A)
# A becomes right child of G (which was Nil); G becomes the left child of P;
# G goes red; P goes black

# Case D (mirror of B)
# a becomes the right child of G; b becomes the left child of P; G becomes the left child of N; P becomes the right child of N
# G goes red; N goes black