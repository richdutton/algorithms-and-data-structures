# pylint:disable=E1135
# pylint:disable=W0212
# pylint:disable=C0103
from enum import Enum


InsertionPoint = Enum('InsertionPoint', '_left _right root')


# todo: would it be better if the tree were responsible for the rotations?
#       rather than keeping reference to parent would it be easier to check balance of child rather than self?
#
class Node:
    def __init__(self, key, parent, insertion_point):
        self._key = key
        self._left = None
        self._right = None
        self._parent = parent
        self._insertion_point = insertion_point

        self._balance_factor = 0
        self._height = 1

    def _insert_key(self, key):
        assert key != self._key

        insertion_point = InsertionPoint._left if key < self._key else InsertionPoint._right
        insertions = [insertion_point]

        if getattr(self, insertion_point.name) is None:
            setattr(self, insertion_point.name, Node(key, self, insertion_point))
        else:
            insertions.extend(getattr(self, insertion_point.name).insert(key))

        return insertions

    def _right_rotation(self):
        # todo: if this never fires then we can simlify the line that follows it to self._left._right = self
        assert self._left._right is None
        old_left = self._left
        self._left._right, self._left = self, self._left._right

        setattr(self._parent, self._insertion_point.name, old_left)
        old_left._insertion_point = self._insertion_point
        old_left._parent = self._parent

        self._parent = old_left
        self._insertion_point = InsertionPoint._right

        # todo: assuming here that don't have to rebalance self again (related to assumption above)
        self._update_height_and_balance_factor(propagate=True)

    # todo: augment with new logic in right rotation when have tested same and fixed balance factor
    def _left_rotation(self):
        assert self._right._right is None
        self._right._left = self
        setattr(self._parent, self._insertion_point.name, self._right)

    # todo: left-right and right-left. address todo above and test left and right first though
    def _rebalance(self, insertions):
        assert len(insertions) >= 2
        if insertions[0] == InsertionPoint._left:
            if insertions[1] == InsertionPoint._left:
                self._right_rotation()
            else:
                pass
        else:
            if insertions[1] == InsertionPoint._left:
                pass
            else:
                self._left_rotation()

    def insert(self, key):
        insertions = self._insert_key(key)

        if self._update_height_and_balance_factor(propagate=False):
            self._rebalance(insertions)

        return insertions

    def __contains__(self, key):
        if key == self._key:
            return True
        elif key < self._key:
            return False if self._left is None else key in self._left
        else:
            return False if self._right is None else key in self._right

    def _update_height_and_balance_factor(self, propagate):
        left_height = self._left._height if self._left is not None else 0
        right_height = self._right._height if self._right is not None else 0

        self._height = 1 + max(left_height, right_height)
        self._balance_factor = left_height - right_height

        if propagate and isinstance(self._parent, Node):
            self._parent._update_height_and_balance_factor(propagate)

        return abs(self._balance_factor) > 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key, self, InsertionPoint.root)
        else:
            self.root.insert(key)

    def __contains__(self, key):
        return False if self.root is None else key in self.root
