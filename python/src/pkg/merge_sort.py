# todo: this is untested and may contain subtle bugs


def _copy_array(array, helper, low, high):
    for index in range(low, high + 1):
        helper[index] = array[index]


def _merge(array, helper, low, middle, high):
    _copy_array(array, helper, low, high)

    helper_left = low
    helper_right = middle + 1
    current = low

    while helper_left <= middle and helper_right <= high:
        if helper[helper_left] <= helper[helper_right]:
            array[current] = helper[helper_left]
            helper_left += 1
        else:
            array[current] = helper[helper_right]
            helper_right += 1
        current += 1

    remaining = middle + 1 - helper_left
    for index in range(remaining):
        array[current + index] = helper[helper_left + index]


def merge_sort_(array, helper, low, high):
    if low < high:
        middle = (low + high) // 2
        merge_sort_(array, helper, low, middle)
        merge_sort_(array, helper, middle + 1, high)
        _merge(array, helper, low, middle, high)


def merge_sort(array):
    assert array is not None and isinstance(array, list)

    helper = [None] * len(array)
    merge_sort_(array, helper, 0, len(array) - 1)

    return array
