#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None
    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    # max number of comparisons is log2(n)
    comparisons = int(math.ceil(math.log(len(array), 2)))

    for step in range(comparisons):
        index = (right + left) // 2
        if array[index] == item:
            return index
        elif left != right:
            if array[index] > item:
                right = index - 1
            elif array[index] < item:
                left = index + 1
        elif left == right:
            break
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    if left == None or right == None:
        left = 0
        right = len(array) - 1
    index = (right + left) // 2
    if array[index] == item:
            return index
    elif left != right:
        if array[index] > item:
            return binary_search_recursive(array, item, left, index - 1)
        elif array[index] < item:
            return binary_search_recursive(array, item, index + 1, right)
    return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
