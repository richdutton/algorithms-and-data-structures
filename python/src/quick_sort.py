# from random import randint


def quick_sort(array):
    assert array is not None

    if len(array) < 2:
        return array

    # todo:: this seems to be a mix of in place and not. kinda surprised it works
    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    pivot_index = len(array) // 2  # randint(0, length) + start_index
    pivot = array[pivot_index]

    left_array = []  # [None] * (pivot_index - 0)
    right_array = []  # [None] * (len(array) - pivot_index)
    for index, element in enumerate(array):
        if index != pivot_index:
            target_array = left_array if element < pivot else right_array
            target_array.append(element)

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)
