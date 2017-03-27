# pylint:disable=E1135
# pylint:disable=W0212
# pylint:disable=C0103
from enum import Enum


Direction = Enum('Direction', '_left _right _down')
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

    @staticmethod
    def _node_height(node):
        return node._height if node is not None else 0

    def _update_height_and_balance_factor(self):
        left_height = self._node_height(self._left)
        right_height = self._node_height(self._right)

        self._height = 1 + max(left_height, right_height)
        self._balance_factor = left_height - right_height

        return abs(self._balance_factor) > 1

    @property
    def _insertion_point(self):
        return (Direction._down if isinstance(self._parent, AVLTree)
                else (Direction._left if self._parent._left is self else Direction._right))

    def _rotate_right_or_left(self, direction):
        other_direction = Direction._right if direction is Direction._left else Direction._left

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

    def _rotate(self):
        # TODO: we've already checked balance factor but we're going to have to check it again here. is that optimal?
        if self._node_height(self._left) - self._node_height(self._right) > 1:
            # self._left must not be none given above
            assert self._left is not None
            if self._node_height(self._left._left) >= self._node_height(self._left._right):
                self._rotate_right_or_left(Direction._right)
            else:
                self._left._rotate_right_or_left(Direction._left)
                self._rotate_right_or_left(Direction._right)
        else:
            # if we need to rebalance then either left is overweight or right. it's not left per above
            assert self._right is not None and self._node_height(self._right) - self._node_height(self._left) > 1
            if self._node_height(self._right._right) >= self._node_height(self._right._left):
                self._rotate_right_or_left(Direction._left)
            else:
                self._right._rotate_right_or_left(Direction._right)
                self._rotate_right_or_left(Direction._left)

    def _rebalance(self):
        if self._update_height_and_balance_factor() and not self._do_not_rebalance:
            AVLTree.rebalanced = True
            self._rotate()
            # always recurse to ensure height and b.f. are updated (even though recursive rotations unnecessary for insert)
            self._parent._rebalance()

    def _insert_key(self, key):
        assert key != self._key

        insertion_point = Direction._left if key < self._key else Direction._right
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


# TODO: test double rotation
#       remove do_not_rebalance hack in favor of monkeypatching or just careful construction of trees
#       AVLTree.rebalanced hack (is there a better way?)
#       potentially move most of logic from node into tree
#       rather than keeping reference to parent would it be easier to check balance of child rather than self?
#
class AVLTree:
    rebalanced = False

    def __init__(self, rebalance):
        self._down = None
        # TODO: this is lame; could just monkeypatch it
        self._rebalance = rebalance
        AVLTree.rebalanced = False

    def insert(self, key):
        self.rebalanced = False

        if not self._down:
            self._down = Node(key, self, not self._rebalance)
        else:
            self._down.insert(key)

    def __contains__(self, key):
        return False if self._down is None else key in self._down
