def get_index_of_smallest_item(array):
    smallest_index_and_element = -1, float('inf')

    for index, element in enumerate(array):
        if element and element < smallest_index_and_element[1]:
            smallest_index_and_element = index, element

    return smallest_index_and_element


def selection_sort(array):
    assert array is not None

    unsorted_array = array.copy()
    sorted_array = [None] * len(unsorted_array)

    for iteration, _ in enumerate(unsorted_array):
        index, element = get_index_of_smallest_item(unsorted_array)
        sorted_array[iteration] = element
        unsorted_array[index] = None

    return sorted_array
