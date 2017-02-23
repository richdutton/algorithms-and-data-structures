class Node:
    def __init__(self, value, next_):
        self.next_ = next_
        self.value = value


def has_cycles(node):
    assert node is not None

    slow = fast = node
    while True:
        slow = slow.next_
        fast = fast.next_

        if fast is None:
            return False

        fast = fast.next_
        if fast is None:
            return False

        if fast == slow:
            return True
