# pylint:disable=E1135
# pylint:disable=W0212
# pylint:disable=C0103
from enum import Enum


InsertionPoint = Enum('InsertionPoint', '_left _right root')
_REBALANCE = True


class Node:
    def __init__(self, key, parent, do_not_rebalance):
        self._key = key
        self._left = None
        self._right = None
        self._parent = parent
        self._do_not_rebalance = do_not_rebalance

        self._balance_factor = 0
        self._height = 1

    def _update_height_and_balance_factor(self):
        left_height = self._node_height(self._left)
        right_height = self._node_height(self._right)

        self._height = 1 + max(left_height, right_height)
        self._balance_factor = left_height - right_height

        return abs(self._balance_factor) > 1

    @property
    def _insertion_point(self):
        return (InsertionPoint.root if isinstance(self._parent, AVLTree)
                else (InsertionPoint._left if self._parent._left is self else InsertionPoint._right))

    def _rotate_right_or_left(self, direction):
        other_direction = InsertionPoint._right if direction is InsertionPoint._left else InsertionPoint._left

        x = self
        y = getattr(self, other_direction.name)

        y._parent = x._parent
        setattr(x._parent, self._insertion_point.name, y)
        setattr(x, other_direction.name, getattr(y, direction.name))
        if getattr(y, direction.name) is not None:
            getattr(y, direction.name)._parent = x
        x._parent = y
        setattr(y, direction.name, x)

        self._update_height_and_balance_factor()

    def _rotate_right(self):
        self._rotate_right_or_left(InsertionPoint._right)
        # x = self
        # y = self._left

        # y._parent = x._parent
        # setattr(x._parent, self._insertion_point.name, y)
        # x._left = y._right
        # if y._right is not None:
        #     y._right._parent = x
        # x._parent = y
        # y._right = x

        # self._update_height_and_balance_factor()

    def _rotate_right_old(self):
        old_left = self._left
        self._left._right, self._left = self, self._left._right  # 1a,b
        if self._left is not None:
            self._left.parent = self

        setattr(self._parent, self._insertion_point.name, old_left)  # 2
        old_left._parent = self._parent  # 3
        self._parent = old_left  # 4

        # TODO: could this be moved to _rotate or would that break double rotations?
        self._update_height_and_balance_factor()

    def _rotate_left(self):
        assert self._right._right is None
        # self._right._left = self
        # setattr(self._parent, self._insertion_point.name, self._right)

    @staticmethod
    def _node_height(node):
        return node._height if node is not None else 0

    def _rotate(self):
        # TODO: we've already checked balance factor but we're going to have to check it again here. is that optimal?
        if self._node_height(self._left) - self._node_height(self._right) > 1:
            # self._left must not be none given above
            assert self._left is not None
            if self._node_height(self._left._left) >= self._node_height(self._left._right):
                self._rotate_right()
            else:
                self._left._left_rotation()
                self._rotate_right()
        else:
            # if we need to rebalance then either left is overweight or right. it's not left per above
            assert self._right is not None and self._node_height(self._right) - self._node_height(self._left) > 1
            if self._node_height(self._right._right) >= self._node_height(self._right._left):
                self._rotate_left()
            else:
                self._right._right_rotation()
                self._rotate_left()

    def _rebalance(self):
        if self._update_height_and_balance_factor() and not self._do_not_rebalance:
            AVLTree.rebalanced = True
            self._rotate()
            # always recurse to ensure height and b.f. are updated (even though recursive rotations unnecessary for insert)
            self._parent._rebalance()

    def _insert_key(self, key):
        assert key != self._key

        insertion_point = InsertionPoint._left if key < self._key else InsertionPoint._right
        if getattr(self, insertion_point.name) is None:
            setattr(self, insertion_point.name, Node(key, self, self._do_not_rebalance))
        else:
            getattr(self, insertion_point.name).insert(key)

    def insert(self, key):
        self._insert_key(key)
        self._rebalance()

    def __contains__(self, key):
        if key == self._key:
            return True
        elif key < self._key:
            return False if self._left is None else key in self._left
        else:
            return False if self._right is None else key in self._right


# TODO: clean up right rotation
#       implement _left_rotation
#        test double rotation
#       remove do_not_rebalance hack in favor of monkeypatching or just careful construction of trees
#       AVLTree.rebalanced hack (is there a better way?)
#       potentially move most of logic from node into tree
#       rather than keeping reference to parent would it be easier to check balance of child rather than self?#
#
class AVLTree:
    rebalanced = False

    def __init__(self, rebalance):
        self.root = None
        # TODO: this is lame; could just monkeypatch it
        self._rebalance = rebalance
        AVLTree.rebalanced = False

    def insert(self, key):
        self.rebalanced = False

        if not self.root:
            self.root = Node(key, self, not self._rebalance)
        else:
            self.root.insert(key)

    def __contains__(self, key):
        return False if self.root is None else key in self.root
