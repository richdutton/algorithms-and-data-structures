# pylint:disable=E1135
# pylint:disable=W0212
# pylint:disable=C0103
from enum import Enum


InsertionPoint = Enum('InsertionPoint', '_left _right root')
_REBALANCE = True


# TODO: rather than keeping reference to parent would it be easier to check balance of child rather than self?
#
class Node:
    def __init__(self, key, parent, insertion_point, do_not_rebalance):
        self._key = key
        self._left = None
        self._right = None
        self._parent = parent
        self._insertion_point = insertion_point
        self._do_not_rebalance = do_not_rebalance

        self._balance_factor = 0
        self._height = 1

    def _insert_key(self, key):
        assert key != self._key

        insertion_point = InsertionPoint._left if key < self._key else InsertionPoint._right
        insertions = [insertion_point]

        if getattr(self, insertion_point.name) is None:
            setattr(self, insertion_point.name, Node(key, self, insertion_point, self._do_not_rebalance))
        else:
            insertions.extend(getattr(self, insertion_point.name).insert(key))

        return insertions

    def _right_rotation(self):
        old_left = self._left
        self._left._right, self._left = self, self._left._right  # 1a,b
        if self._left is not None:
            self._left.parent = self
            self._left._insertion_point = InsertionPoint._left

        setattr(self._parent, self._insertion_point.name, old_left)  # 2
        old_left._insertion_point = self._insertion_point
        old_left._parent = self._parent  # 3

        self._parent = old_left  # 4
        self._insertion_point = InsertionPoint._right

        self._update_height_and_balance_factor()

    # TODO: augment with new logic in right rotation when have tested and clarified same
    def _left_rotation(self):
        assert self._right._right is None
        self._right._left = self
        setattr(self._parent, self._insertion_point.name, self._right)

    def _rotation(self, insertions):
        assert len(insertions) >= 2

        # TODO: we've already checked balance factor but we're going to have to check it again here
        # if height(node.left) >= 2 + height(node.right):
        if insertions[0] == InsertionPoint._left:
            # if height(node.left.left) >= height(node.left.right):
            if insertions[1] == InsertionPoint._left:
                self._right_rotation()
            else:
                self._left._left_rotation()
                self._right_rotation()
        else:  # elif height(node.right) >= 2 + height(node.left):
            # if height(node.right.right) >= height(node.right.left):
            if insertions[1] == InsertionPoint._right:
                self._left_rotation()
            else:
                self._right._right_rotation()
                self._left_rotation()

    def _rebalance(self, insertions):
        if self._update_height_and_balance_factor() and not self._do_not_rebalance:
            AVLTree.rebalanced = True
            self._rotation(insertions)
            self._parent._rebalance(insertions)  # TODO: 0% sure insertions is valid at this stage

    def insert(self, key):
        insertions = self._insert_key(key)
        self._rebalance(insertions)

        return insertions

    def __contains__(self, key):
        if key == self._key:
            return True
        elif key < self._key:
            return False if self._left is None else key in self._left
        else:
            return False if self._right is None else key in self._right

    def _update_height_and_balance_factor(self):
        left_height = self._left._height if self._left is not None else 0
        right_height = self._right._height if self._right is not None else 0

        self._height = 1 + max(left_height, right_height)
        self._balance_factor = left_height - right_height

        return abs(self._balance_factor) > 1


# TODO: move away from InsertionPoint in favor of identity check
#       lose the insertion point / insertions
#       implement _left_rotation
#       remove do_not_rebalance hack in favor of monkeypatching or just careful construction of trees
#       AVLTree.rebalanced hack (is there a better way?)
#       potentially move most of logic from node into tree
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
            self.root = Node(key, self, InsertionPoint.root, not self._rebalance)
        else:
            self.root.insert(key)

    def __contains__(self, key):
        return False if self.root is None else key in self.root
