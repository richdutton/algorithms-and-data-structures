#!/usr/bin/env python
# http://codexpi.com/quicksort-python-iterative-recursive-implementations/


def quick_sort_iterative(list_, left, right):
    temp_stack = []
    temp_stack.append((left, right))

    # Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_, left, right)
        # If items in the left of the pivot push them to the stack
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        # If items in the right of the pivot push them to the stack
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))


def quick_sort_recursive(list_, left, right):
    if right <= left:
        return
    else:
        # Get pivot
        piv = partition(list_, left, right)
        # Sort left side of pivot
        quick_sort_recursive(list_, left, piv - 1)
        # Sort right side of pivot
        quick_sort_recursive(list_, piv + 1, right)


def partition(list_, left, right):
    # Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right

    while 1:
        while i <= j and list_[i] <= piv:
            i += 1
        while j >= i and list_[j] >= piv:
            j -= 1
        if j <= i:
            break
        # xchange items
        list_[i], list_[j] = list_[j], list_[i]
    # Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j
