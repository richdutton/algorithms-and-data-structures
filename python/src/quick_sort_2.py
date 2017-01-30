# todo: the non-in-place might have been failling tests (though it should be generally sound otherwise)
# and the in-place version hasn't been run against all tests

import random


# alternative implementations:
#
#    smaller_elements = [element for index, element in enumerate(array) if index != pivot_index and element <= pivot]
#    larger_elements = [element for index, element in enumerate(array) if  index != pivot_index and element > pivot]
#                if element <= pivot:
#                    smaller_elements.append(element)
#                else:
#                    larger_elements.append(element)
def quick_sort(array):
    assert array is not None

    if len(array) < 2:
        return array

    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]

    smaller_elements = larger_elements = []
    for index, element in enumerate(array):
        if index != pivot_index:
            (smaller_elements if element <= pivot else larger_elements).append(element)

    return quick_sort(smaller_elements) + [pivot] + quick_sort(larger_elements)


def _partition(array, start_index, end_index):
    pivot_index = (end_index + start_index) // 2
    pivot = array[pivot_index]

    left_index, right_index = start_index, end_index
    while left_index <= right_index:  # added =
        while array[left_index] < pivot:
            left_index += 1
        while array[right_index] > pivot:
            right_index -= 1

        if left_index <= right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            left_index, right_index = left_index + 1, right_index - 1

    # todo: why is this correct when we move the pivot?
    return left_index  # pivot_index


def _in_place_quick_sort(array, start_index, end_index):
    # if start_index < end_index:
    pivot_index = _partition(array, start_index, end_index)
    # todo: comparison could be in partition
    if start_index < pivot_index - 1:  # adjusted comparison from !=
        _in_place_quick_sort(array, start_index, pivot_index - 1)  # adjusted end index
    if pivot_index < end_index:
        _in_place_quick_sort(array, pivot_index, end_index)


def in_place_quick_sort(array):
    assert array is not None
    _in_place_quick_sort(array, 0, len(array) - 1)

    # maintain equivalent interface to quick_sort
    return array

# void quickSort(int[] arr, int left, int right) {
#     int index = partition(arr, left, right);
#     if (left < index - 1) {
#         quickSort(arr, left, index - 1);
#     }
#     if (index < right) {
#         quickSort(arr, index, right);
#     }
# }

# int partition(int[] arr, int left, int right) {
#     int pivot = arr[(left + right) / 2];
#     while (left <= right) {
#         while (arr[left] < pivot) left ++;
#         while (arr[right] > pivot) right--;

#         if (left <= right) {
#             swap(arr, left, right);
#             left++;
#             right--;
#         }
#     }
#     return left;
# }