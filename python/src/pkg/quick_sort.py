from random import randint


# alternative implementations:
#
#    smaller_elements = [element for index, element in enumerate(array) if index != pivot_index and element <= pivot]
#    larger_elements = [element for index, element in enumerate(array) if  index != pivot_index and element > pivot]
#                if element <= pivot:
#                    smaller_elements.append(element)
#                else:
#                    larger_elements.append(element)
def quick_sort(array):
    assert array is not None and isinstance(array, list)

    if len(array) < 2:
        return array

    pivot_index = randint(0, len(array) - 1)
    pivot = array[pivot_index]

    smaller_elements = []
    larger_elements = []
    for index, element in enumerate(array):
        if index != pivot_index:
            (smaller_elements if element < pivot else larger_elements).append(element)

    return quick_sort(smaller_elements) + [pivot] + quick_sort(larger_elements)


def _partition(array, start_index, end_index):
    pivot_index = (end_index + start_index) // 2
    pivot = array[pivot_index]

    left_index, right_index = start_index, end_index
    while left_index <= right_index:
        # notice that left_index or right_index can == pivot_index, after loopsn
        while array[left_index] < pivot:
            left_index += 1
        while array[right_index] > pivot:
            right_index -= 1

        if left_index <= right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index, right_index = left_index + 1, right_index - 1

    return left_index


def _in_place_quick_sort(array, start_index, end_index):
    if start_index >= end_index:
        return

    pivot_index = _partition(array, start_index, end_index)

    _in_place_quick_sort(array, start_index, pivot_index - 1)
    _in_place_quick_sort(array, pivot_index, end_index)


def in_place_quick_sort(array):
    assert array is not None and isinstance(array, list)
    _in_place_quick_sort(array, 0, len(array) - 1)

    # maintain equivalent interface to quick_sort
    return array


# http://codexpi.com/quicksort-python-iterative-recursive-implementations/


def _partition_alternate(list_, left, right):
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


def _quick_sort_iterative(list_, left, right):
    temp_stack = []
    temp_stack.append((left, right))

    # Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = _partition_alternate(list_, left, right)
        # If items in the left of the pivot push them to the stack
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        # If items in the right of the pivot push them to the stack
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))


def quick_sort_iterative(list_):
    assert list_ is not None and isinstance(list_, list)
    # catch [] and prevent index error
    if list_:
        _quick_sort_iterative(list_, 0, len(list_) - 1)
    return list_


def _quick_sort_alternate(list_, left, right):
    if right <= left:
        return
    else:
        # Get pivot
        piv = _partition_alternate(list_, left, right)
        # Sort left side of pivot
        _quick_sort_alternate(list_, left, piv - 1)
        # Sort right side of pivot
        _quick_sort_alternate(list_, piv + 1, right)

    return list_


def quick_sort_alternate(list_):
    assert list_ is not None and isinstance(list_, list)
    _quick_sort_alternate(list_, 0, len(list_) - 1)
    return list_
