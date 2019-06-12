#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    for index, value in enumerate(array): # loop array til item is found
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if item == array[index]:
        return index
    else: # if n is an integer larger than the base case
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


# TODO: Finish white boarding this solution, edge case is broken.
def binary_search_iterative(array, item):
    left = 0
    right = len(array)
    while (left <= right):
        middle_index = len(list) // 2 # // returns the biggest int, not float.
        if item == array[middle_index]:
            return middle_index
        if item < array[middle_index]:
            left = middle_index + 1
            # print(f"new left: {left}")
        elif item > array[middle_index]:
            right = middle_index - 1
            # print(f"new right: {right}")
    return None

    # My old Psuedocode - broken.
    # middle_index = len of list // 2
    # while 3, 5
    # compare the element at middle_index to the item
    # if they're equal, return the middle_index.
    # if middle_index < item

def binary_search_recursive(array, item, left=None, right=None):
    # The set up for the come up 🔥
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1

    # Edge Case
    if right - left <= 0:
        return None
    
    # The Crux of our Algorithm.
    middle_index = (right + left) // 2

    if item == array[middle_index]:
        return middle_index
    elif item < array[middle_index]:
        return binary_search_recursive(array, item, left, middle_index-1)
    elif item > array[middle_index]:
        return binary_search_recursive(array, item, middle_index+1, right)