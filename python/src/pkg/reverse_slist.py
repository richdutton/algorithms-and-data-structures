class Node:
    def __init__(self, value, next_):
        self.next_ = next_
        self.value = value


def reverse_slist(node):
    assert node is not None

    previous = None
    current = node
    next_ = current.next_
    while next_ is not None:
        current.next_ = previous
        previous = current
        current = next_
        next_ = next_.next_
    current.next_ = previous

    return current
